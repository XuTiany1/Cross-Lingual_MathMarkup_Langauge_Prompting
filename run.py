import os
import argparse
import json
import evaluate
import torch
from tqdm import tqdm
from vllm import LLM, SamplingParams
from tasks.mgsm import mgsm
import numpy as np
import textwrap  # NEW: for cleaning up example strings
from transformers import AutoTokenizer

# Set the GPU device (if available)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# ===================================================================
# Define arguments and new parameter for branch languages.
args = argparse.Namespace(
    task='MGSM',
    lang='en',  # Default language; will be overwritten in the loop if needed
    languages=['sot'], #vai
    model_type='gemma_12b',
    solve_method='CLP',
    understand_langauge='native_understand',
    run_name='english',
    understander_lang='en',  # Default; not used because we have a branch list below.
    shot=2,
    model_max_token=4094,
    model_temperature=0.5,
    total_dataset_sample=250   # For testing; later increase as needed.
)

args.understander_lang_list = ['es', 'fr', 'ja']

# Override from CLI if needed
parser = argparse.ArgumentParser()
parser.add_argument('--lang', type=str, default='en')
cli_args, _ = parser.parse_known_args()
args.lang = cli_args.lang

# ===================================================================
# Set up output folder and evaluation metric
run_folder = os.path.join("MGSM_HIGH_result")
os.makedirs(run_folder, exist_ok=True)
exact_match_metric = evaluate.load("exact_match")

# ===================================================================
# Set up the VLLM model
model_name = "google/gemma-3-12b-it"
llm = LLM(
    model=model_name,
    tensor_parallel_size=1,  # Adjust based on your GPU setup
    dtype="bfloat16",
    trust_remote_code=True,
    max_model_len=args.model_max_token
)
tokenizer = AutoTokenizer.from_pretrained(model_name)


# Sampling parameters for generation
sampling_params = SamplingParams(
    temperature=args.model_temperature,
    max_tokens=args.model_max_token,
    top_p=1.0,
    top_k=-1,  # No top-k filtering
)

# ---------------------------------------------------------------------
# Modified helper function: Instead of adding role markers, we just concatenate texts.
def format_chat_prompt(messages):
    # Instead of appending an extra newline, we join and then strip to remove extra whitespace.
    return "\n".join(message["content"][0]["text"].strip() for message in messages).strip()

# Voting helper: extract final numbers from predictions and return the most frequent.
def vote_prediction(task, predictions):
    extracted = []
    for pred in predictions:
        try:
            num = task.extract_final_number(task, pred)
        except Exception:
            num = None
        extracted.append(num)
    freq = {}
    for num in extracted:
        freq[num] = freq.get(num, 0) + 1
    if freq:
        max_freq = max(freq.values())
        candidates = [num for num, count in freq.items() if count == max_freq]
        for num in extracted:
            if num in candidates:
                return num
    return None

final_format = "number"


# ------------------------------------------------------------------------------
# New helper: safe_generate
def safe_generate(prompts, sampling_params, llm, token_limit, tokenizer):
    """
    Truncate every prompt to `token_limit` tokens up front and then call llm.generate.
    """
    # batch‐tokenize with truncation
    encoding = tokenizer(
        prompts,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=token_limit
    )

    # decode back into strings
    truncated_prompts = tokenizer.batch_decode(
        encoding.input_ids,
        skip_special_tokens=True
    )

    # now safe to generate without ever exceeding the model's context window
    return llm.generate(truncated_prompts, sampling_params)






# ===================================================================
# Main Loop: Process each native language in batch.
for lang in args.languages:
    args.lang = lang
    task = mgsm(args)
    args.understander_lang_list = [lang, lang, lang]


    total_count = 0
    # Aggregated accuracy counts per branch (order as in args.understander_lang_list).
    branch_correct_counts = [0] * len(args.understander_lang_list)
    self_consistency_correct_count = 0

    # Prepare directories.
    lang_dir_path = os.path.join(run_folder, args.model_type, args.solve_method, args.understand_langauge, args.run_name, lang)
    os.makedirs(lang_dir_path, exist_ok=True)

    # Log hyperparameters.
    hyperparams_path = os.path.join(lang_dir_path, f"{lang}_hyperparams.log")
    with open(hyperparams_path, "w") as hp:
        hp.write("--- Hyperparameters / Args ---\n")
        for k, v in vars(args).items():
            hp.write(f"{k}: {v}\n")

    result_json_filename = os.path.join(lang_dir_path, f"{lang}_result.jsonl")
    os.makedirs(os.path.dirname(result_json_filename), exist_ok=True)
    visual_json_filename = os.path.join(lang_dir_path, f"{lang}_visualize.jsonl")
    os.makedirs(os.path.dirname(visual_json_filename), exist_ok=True)

    # -------------------------------------------------------------------
    # Prepare questions: gather native and English versions.
    native_questions = []
    english_questions = []
    for idx in tqdm(range(args.total_dataset_sample), desc=f"Collecting examples for {lang}"):
        total_count += 1
        native_q = task.get_input(idx)
        english_q = task.get_english_input(idx)
        native_questions.append(native_q)
        english_questions.append(english_q)

    if args.solve_method == 'CPAL':
        num_branches = len(args.understander_lang_list)
        # Create storage for branch understandings and solver outputs.
        branch_understandings = [[None] * args.total_dataset_sample for _ in range(num_branches)]
        branch_solver_outputs = [[None] * args.total_dataset_sample for _ in range(num_branches)]
        
        # -------------------------------------------------------------------
        # Step 1: Generate branch understandings.
        # For each branch, we use a plain text prompt that instructs the model
        # to output a single chain-of-thought for understanding.
        batch_size_understanding = 25
        for branch_idx, branch_lang in enumerate(args.understander_lang_list):
            prompts = []
            indices = []
            for idx in range(args.total_dataset_sample):
                # --- Modified: Clean up the prompt examples using dedent and strip.
                understand_input = task.understand_prompt(
                    source_language=lang,
                    understander_language=branch_lang,
                    shot=args.shot,
                    native_question=native_questions[idx]
                )

                langauge_name = task.get_langauge_name(branch_lang)
                # Here the prompt is a plain text combining our instruction and the question.
                messages_understand = [
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": (
                            "Do not provide any other reasoning and do not include any conversational markers." +
                            understand_input
                        )}]
                    }
                ]
                prompts.append(format_chat_prompt(messages_understand))
                indices.append(idx)
            for start in tqdm(range(0, len(prompts), batch_size_understanding),
                            desc=f"Understandings for branch {branch_idx+1} ({branch_lang}) for {lang}"):
                end = min(start + batch_size_understanding, len(prompts))
                batch_prompts = prompts[start:end]
                outputs = safe_generate(batch_prompts, sampling_params, llm, args.model_max_token, tokenizer)
                for i, output in enumerate(outputs):
                    branch_understandings[branch_idx][indices[start + i]] = output.outputs[0].text

        # -------------------------------------------------------------------
        # Step 2: Generate branch solver outputs.
        # For each branch, we use a plain text prompt instructing the model to provide
        # a single, continuous chain-of-thought with the final answer.
        batch_size_solver = 25
        for branch_idx, branch_lang in enumerate(args.understander_lang_list):
            prompts = []
            indices = []
            for idx in range(args.total_dataset_sample):
                solver_input = task.solver_prompt(
                    native_question=native_questions[idx],
                    understanding=branch_understandings[branch_idx][idx],
                    understander_language=branch_lang,
                    source_language=lang
                ).replace("{final_format}", final_format)

                solver_input += "\nAnswer:"
                langauge_name = task.get_langauge_name(lang)
                messages_solver = [
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": (
                            "You are a programming expert in " + langauge_name + 
                            ". Do not include any conversational markers or role labels.\n\n" +
                            solver_input
                        )}]
                    }
                ]
                prompts.append(format_chat_prompt(messages_solver))
                indices.append(idx)
            for start in tqdm(range(0, len(prompts), batch_size_solver),
                            desc=f"Solver outputs for branch {branch_idx+1} ({branch_lang}) for {lang}"):
                end = min(start + batch_size_solver, len(prompts))
                batch_prompts = prompts[start:end]
                outputs = safe_generate(batch_prompts, sampling_params, llm, args.model_max_token, tokenizer)

                for i, output in enumerate(outputs):
                    branch_solver_outputs[branch_idx][indices[start + i]] = output.outputs[0].text

        # -------------------------------------------------------------------
        # Step 3: Process outputs, extract predictions, and build a summary.
        records = []
        for idx in range(args.total_dataset_sample):
            try:
                ground_truth = task.ground_truth_answer(idx)
                ground_truth_float = float(ground_truth)
            except Exception:
                ground_truth = None
                ground_truth_float = None

            branch_predictions = []
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                try:
                    pred = task.extract_final_number(task, branch_solver_outputs[branch_idx][idx])
                except Exception:
                    pred = None
                branch_predictions.append(pred)
                try:
                    if pred is not None and ground_truth_float is not None:
                        if float(pred) == ground_truth_float:
                            branch_correct_counts[branch_idx] += 1
                except Exception:
                    pass

            self_consistency_prediction = vote_prediction(task, [branch_solver_outputs[b][idx] for b in range(num_branches)])
            try:
                if self_consistency_prediction is not None and ground_truth_float is not None:
                    if float(self_consistency_prediction) == ground_truth_float:
                        self_consistency_correct_count += 1
            except Exception:
                pass

            summary_lines = []
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                summary_lines.append(f"Branch {branch_idx+1} ({branch_lang}) prediction vs ground truth: {branch_predictions[branch_idx]}/{ground_truth}")
            summary_lines.append("====================================")
            summary_lines.append("")
            summary_lines.append("------ Current Accuracy Summary ------")
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                current_acc = branch_correct_counts[branch_idx] / (idx + 1)
                summary_lines.append(f"Branch {branch_idx+1} ({branch_lang}) Accuracy: {current_acc:.2%}")
            self_consistency_acc_current = self_consistency_correct_count / (idx + 1)
            summary_lines.append(f"Self-consistency Accuracy: {self_consistency_acc_current:.2%}")
            summary_text = "\n".join(summary_lines)

            details_lines = []
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                details_lines.append(f"Branch {branch_idx+1} ({branch_lang}) Understanding: {branch_understandings[branch_idx][idx]}")
                details_lines.append(f"Branch {branch_idx+1} ({branch_lang}) Solver Output: {branch_solver_outputs[branch_idx][idx]}")
            details_text = "\n".join(details_lines)

            # Print the full summary and details.
            print(summary_text)
            print(details_text)
            print("====================================\n")

            record = {
                "question": english_questions[idx],
                "native_question": native_questions[idx],
                "ground_truth": ground_truth,
                "branch_understandings": [
                    {"language": args.understander_lang_list[b], "understanding": branch_understandings[b][idx]}
                    for b in range(num_branches)
                ],
                "branch_solver_outputs": [
                    {"language": args.understander_lang_list[b], "solver_output": branch_solver_outputs[b][idx]}
                    for b in range(num_branches)
                ],
                "summary": summary_text
            }
            records.append(record)
            json_record = json.dumps(record, ensure_ascii=False,
                                    default=lambda o: int(o) if isinstance(o, (np.int64, np.int32)) else o)
            with open(result_json_filename, "a", encoding="utf-8") as fp:
                fp.write(json_record + "\n")
            with open(visual_json_filename, "a", encoding="utf-8") as fp:
                fp.write(json.dumps(record, indent=2, ensure_ascii=False,
                                    default=lambda o: int(o) if isinstance(o, (np.int64, np.int32)) else o) + "\n")
        
        # -------------------------------------------------------------------
        # Aggregated accuracy reporting.
        print("\n------ Aggregated Accuracy Summary ------")
        for branch_idx, branch_lang in enumerate(args.understander_lang_list):
            branch_acc = branch_correct_counts[branch_idx] / args.total_dataset_sample
            print(f"Branch {branch_idx+1} ({branch_lang}) Accuracy: {branch_acc:.2%}")
        self_consistency_acc = self_consistency_correct_count / args.total_dataset_sample
        print(f"Self-consistency Accuracy: {self_consistency_acc:.2%}\n")


    elif args.solve_method == 'CLP':
        num_branches = len(args.understander_lang_list)
        # Create storage for branch understandings and solver outputs.
        branch_understandings = [[None] * args.total_dataset_sample for _ in range(num_branches)]
        branch_solver_outputs = [[None] * args.total_dataset_sample for _ in range(num_branches)]
        
        # -------------------------------------------------------------------
        # Step 1: Generate branch understandings.
        # For each branch, we use a plain text prompt that instructs the model
        # to output a single chain-of-thought for understanding.
        batch_size_understanding = 25
        for branch_idx, branch_lang in enumerate(args.understander_lang_list):
            prompts = []
            indices = []
            for idx in range(args.total_dataset_sample):
                # --- Modified: Clean up the prompt examples using dedent and strip.
                understand_input = task.clp_understand_prompt(
                    source_language=lang,
                    understander_language=branch_lang,
                    shot=args.shot,
                    native_question=native_questions[idx]
                )

                langauge_name = task.get_langauge_name(branch_lang)
                # Here the prompt is a plain text combining our instruction and the question.
                messages_understand = [
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": (
                            "Do not include any conversational markers." +
                            understand_input
                        )}]
                    }
                ]
                prompts.append(format_chat_prompt(messages_understand))
                indices.append(idx)
            for start in tqdm(range(0, len(prompts), batch_size_understanding),
                            desc=f"Understandings for branch {branch_idx+1} ({branch_lang}) for {lang}"):
                end = min(start + batch_size_understanding, len(prompts))
                batch_prompts = prompts[start:end]
                outputs = safe_generate(batch_prompts, sampling_params, llm, args.model_max_token, tokenizer)
                for i, output in enumerate(outputs):
                    branch_understandings[branch_idx][indices[start + i]] = output.outputs[0].text

        # -------------------------------------------------------------------
        # Step 2: Generate branch solver outputs.
        # For each branch, we use a plain text prompt instructing the model to provide
        # a single, continuous chain-of-thought with the final answer.
        batch_size_solver = 25
        for branch_idx, branch_lang in enumerate(args.understander_lang_list):
            prompts = []
            indices = []
            for idx in range(args.total_dataset_sample):
                solver_input = task.clp_solver_prompt(
                    native_question=native_questions[idx],
                    understanding=branch_understandings[branch_idx][idx],
                    understander_language=branch_lang,
                    source_language=lang
                ).replace("{final_format}", final_format)

                solver_input += "\nAnswer:"
                langauge_name = task.get_langauge_name(lang)
                messages_solver = [
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": (
                            "Do not include any conversational markers or role labels.\n\n" +
                            solver_input
                        )}]
                    }
                ]
                prompts.append(format_chat_prompt(messages_solver))
                indices.append(idx)
            for start in tqdm(range(0, len(prompts), batch_size_solver),
                            desc=f"Solver outputs for branch {branch_idx+1} ({branch_lang}) for {lang}"):
                end = min(start + batch_size_solver, len(prompts))
                batch_prompts = prompts[start:end]
                outputs = safe_generate(batch_prompts, sampling_params, llm, args.model_max_token, tokenizer)

                for i, output in enumerate(outputs):
                    branch_solver_outputs[branch_idx][indices[start + i]] = output.outputs[0].text

        # -------------------------------------------------------------------
        # Step 3: Process outputs, extract predictions, and build a summary.
        records = []
        for idx in range(args.total_dataset_sample):
            try:
                ground_truth = task.ground_truth_answer(idx)
                ground_truth_float = float(ground_truth)
            except Exception:
                ground_truth = None
                ground_truth_float = None

            branch_predictions = []
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                try:
                    pred = task.extract_final_number(task, branch_solver_outputs[branch_idx][idx])
                except Exception:
                    pred = None
                branch_predictions.append(pred)
                try:
                    if pred is not None and ground_truth_float is not None:
                        if float(pred) == ground_truth_float:
                            branch_correct_counts[branch_idx] += 1
                except Exception:
                    pass

            self_consistency_prediction = vote_prediction(task, [branch_solver_outputs[b][idx] for b in range(num_branches)])
            try:
                if self_consistency_prediction is not None and ground_truth_float is not None:
                    if float(self_consistency_prediction) == ground_truth_float:
                        self_consistency_correct_count += 1
            except Exception:
                pass

            summary_lines = []
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                summary_lines.append(f"Branch {branch_idx+1} ({branch_lang}) prediction vs ground truth: {branch_predictions[branch_idx]}/{ground_truth}")
            summary_lines.append("====================================")
            summary_lines.append("")
            summary_lines.append("------ Current Accuracy Summary ------")
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                current_acc = branch_correct_counts[branch_idx] / (idx + 1)
                summary_lines.append(f"Branch {branch_idx+1} ({branch_lang}) Accuracy: {current_acc:.2%}")
            self_consistency_acc_current = self_consistency_correct_count / (idx + 1)
            summary_lines.append(f"Self-consistency Accuracy: {self_consistency_acc_current:.2%}")
            summary_text = "\n".join(summary_lines)

            details_lines = []
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                details_lines.append(f"Branch {branch_idx+1} ({branch_lang}) Understanding: {branch_understandings[branch_idx][idx]}")
                details_lines.append(f"Branch {branch_idx+1} ({branch_lang}) Solver Output: {branch_solver_outputs[branch_idx][idx]}")
            details_text = "\n".join(details_lines)

            # Print the full summary and details.
            print(summary_text)
            print(details_text)
            print("====================================\n")

            record = {
                "question": english_questions[idx],
                "native_question": native_questions[idx],
                "ground_truth": ground_truth,
                "branch_understandings": [
                    {"language": args.understander_lang_list[b], "understanding": branch_understandings[b][idx]}
                    for b in range(num_branches)
                ],
                "branch_solver_outputs": [
                    {"language": args.understander_lang_list[b], "solver_output": branch_solver_outputs[b][idx]}
                    for b in range(num_branches)
                ],
                "summary": summary_text
            }
            records.append(record)
            json_record = json.dumps(record, ensure_ascii=False,
                                    default=lambda o: int(o) if isinstance(o, (np.int64, np.int32)) else o)
            with open(result_json_filename, "a", encoding="utf-8") as fp:
                fp.write(json_record + "\n")
            with open(visual_json_filename, "a", encoding="utf-8") as fp:
                fp.write(json.dumps(record, indent=2, ensure_ascii=False,
                                    default=lambda o: int(o) if isinstance(o, (np.int64, np.int32)) else o) + "\n")
        
        # -------------------------------------------------------------------
        # Aggregated accuracy reporting.
        print("\n------ Aggregated Accuracy Summary ------")
        for branch_idx, branch_lang in enumerate(args.understander_lang_list):
            branch_acc = branch_correct_counts[branch_idx] / args.total_dataset_sample
            print(f"Branch {branch_idx+1} ({branch_lang}) Accuracy: {branch_acc:.2%}")
        self_consistency_acc = self_consistency_correct_count / args.total_dataset_sample
        print(f"Self-consistency Accuracy: {self_consistency_acc:.2%}\n")


    elif args.solve_method == 'mathML_NEW':
        num_branches = len(args.understander_lang_list)
        # Create storage for branch understandings and solver outputs.
        branch_understandings = [[None] * args.total_dataset_sample for _ in range(num_branches)]
        branch_solver_outputs = [[None] * args.total_dataset_sample for _ in range(num_branches)]
        
        # -------------------------------------------------------------------
        # Step 1: Generate branch understandings.
        # For each branch, we use a plain text prompt that instructs the model
        # to output a single chain-of-thought for understanding.
        batch_size_understanding = 25
        for branch_idx, branch_lang in enumerate(args.understander_lang_list):
            prompts = []
            indices = []
            for idx in range(args.total_dataset_sample):
                # --- Modified: Clean up the prompt examples using dedent and strip.
                understand_input = task.mathML_understand_prompt(
                    source_language=lang,
                    understander_language=branch_lang,
                    shot=args.shot,
                    native_question=native_questions[idx]
                )

                langauge_name = task.get_langauge_name(branch_lang)
                # Here the prompt is a plain text combining our instruction and the question.
                messages_understand = [
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": (
                            "Do not include any conversational markers. Do not provide the final answer" +
                            understand_input
                        )}]
                    }
                ]
                prompts.append(format_chat_prompt(messages_understand))
                indices.append(idx)
            for start in tqdm(range(0, len(prompts), batch_size_understanding),
                            desc=f"Understandings for branch {branch_idx+1} ({branch_lang}) for {lang}"):
                end = min(start + batch_size_understanding, len(prompts))
                batch_prompts = prompts[start:end]
                outputs = safe_generate(batch_prompts, sampling_params, llm, args.model_max_token, tokenizer)
                for i, output in enumerate(outputs):
                    branch_understandings[branch_idx][indices[start + i]] = output.outputs[0].text

        # -------------------------------------------------------------------
        # Step 2: Generate branch solver outputs.
        # For each branch, we use a plain text prompt instructing the model to provide
        # a single, continuous chain-of-thought with the final answer.
        batch_size_solver = 25
        for branch_idx, branch_lang in enumerate(args.understander_lang_list):
            prompts = []
            indices = []
            for idx in range(args.total_dataset_sample):
                solver_input = task.mathML_solver_prompt(
                    native_question=native_questions[idx],
                    understanding=branch_understandings[branch_idx][idx],
                    understander_language=branch_lang,
                    source_language=lang
                ).replace("{final_format}", final_format)

                solver_input += "\nAnswer:"
                langauge_name = task.get_langauge_name(lang)
                messages_solver = [
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": (
                            "Do not include any conversational markers or role labels.\n\n" +
                            solver_input
                        )}]
                    }
                ]
                prompts.append(format_chat_prompt(messages_solver))
                indices.append(idx)
            for start in tqdm(range(0, len(prompts), batch_size_solver),
                            desc=f"Solver outputs for branch {branch_idx+1} ({branch_lang}) for {lang}"):
                end = min(start + batch_size_solver, len(prompts))
                batch_prompts = prompts[start:end]
                outputs = safe_generate(batch_prompts, sampling_params, llm, args.model_max_token, tokenizer)

                for i, output in enumerate(outputs):
                    branch_solver_outputs[branch_idx][indices[start + i]] = output.outputs[0].text

        # -------------------------------------------------------------------
        # Step 3: Process outputs, extract predictions, and build a summary.
        records = []
        for idx in range(args.total_dataset_sample):
            try:
                ground_truth = task.ground_truth_answer(idx)
                ground_truth_float = float(ground_truth)
            except Exception:
                ground_truth = None
                ground_truth_float = None

            branch_predictions = []
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                try:
                    pred = task.extract_final_number(task, branch_solver_outputs[branch_idx][idx])
                except Exception:
                    pred = None
                branch_predictions.append(pred)
                try:
                    if pred is not None and ground_truth_float is not None:
                        if float(pred) == ground_truth_float:
                            branch_correct_counts[branch_idx] += 1
                except Exception:
                    pass

            self_consistency_prediction = vote_prediction(task, [branch_solver_outputs[b][idx] for b in range(num_branches)])
            try:
                if self_consistency_prediction is not None and ground_truth_float is not None:
                    if float(self_consistency_prediction) == ground_truth_float:
                        self_consistency_correct_count += 1
            except Exception:
                pass

            summary_lines = []
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                summary_lines.append(f"Branch {branch_idx+1} ({branch_lang}) prediction vs ground truth: {branch_predictions[branch_idx]}/{ground_truth}")
            summary_lines.append("====================================")
            summary_lines.append("")
            summary_lines.append("------ Current Accuracy Summary ------")
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                current_acc = branch_correct_counts[branch_idx] / (idx + 1)
                summary_lines.append(f"Branch {branch_idx+1} ({branch_lang}) Accuracy: {current_acc:.2%}")
            self_consistency_acc_current = self_consistency_correct_count / (idx + 1)
            summary_lines.append(f"Self-consistency Accuracy: {self_consistency_acc_current:.2%}")
            summary_text = "\n".join(summary_lines)

            details_lines = []
            for branch_idx, branch_lang in enumerate(args.understander_lang_list):
                details_lines.append(f"Branch {branch_idx+1} ({branch_lang}) Understanding: {branch_understandings[branch_idx][idx]}")
                details_lines.append(f"Branch {branch_idx+1} ({branch_lang}) Solver Output: {branch_solver_outputs[branch_idx][idx]}")
            details_text = "\n".join(details_lines)

            # Print the full summary and details.
            print(summary_text)
            print(details_text)
            print("====================================\n")

            record = {
                "question": english_questions[idx],
                "native_question": native_questions[idx],
                "ground_truth": ground_truth,
                "branch_understandings": [
                    {"language": args.understander_lang_list[b], "understanding": branch_understandings[b][idx]}
                    for b in range(num_branches)
                ],
                "branch_solver_outputs": [
                    {"language": args.understander_lang_list[b], "solver_output": branch_solver_outputs[b][idx]}
                    for b in range(num_branches)
                ],
                "summary": summary_text
            }
            records.append(record)
            json_record = json.dumps(record, ensure_ascii=False,
                                    default=lambda o: int(o) if isinstance(o, (np.int64, np.int32)) else o)
            with open(result_json_filename, "a", encoding="utf-8") as fp:
                fp.write(json_record + "\n")
            with open(visual_json_filename, "a", encoding="utf-8") as fp:
                fp.write(json.dumps(record, indent=2, ensure_ascii=False,
                                    default=lambda o: int(o) if isinstance(o, (np.int64, np.int32)) else o) + "\n")
        
        # -------------------------------------------------------------------
        # Aggregated accuracy reporting.
        print("\n------ Aggregated Accuracy Summary ------")
        for branch_idx, branch_lang in enumerate(args.understander_lang_list):
            branch_acc = branch_correct_counts[branch_idx] / args.total_dataset_sample
            print(f"Branch {branch_idx+1} ({branch_lang}) Accuracy: {branch_acc:.2%}")
        self_consistency_acc = self_consistency_correct_count / args.total_dataset_sample
        print(f"Self-consistency Accuracy: {self_consistency_acc:.2%}\n")



    elif args.solve_method == 'mathML':
        # ----- Baseline Chain-of-Thought (CoT) method with multiple branches -----
        print("Math ML testing")
        # Use the list of branch languages to determine how many CoT samples to generate.
        list_of_languages = args.understander_lang_list
        list_of_languages = ['en', 'en', 'en']
        num_branches = len(list_of_languages)
        
        # Initialize storage: one output list per branch.
        branch_solver_outputs = [ [None] * args.total_dataset_sample for _ in range(num_branches) ]
        
        batch_size_cot = 25  # Batch size can be adjusted.
        
        # For each branch, generate a solver output using branch-specific prompts.
        for branch_idx, branch_lang in enumerate(list_of_languages):
            # Attempt to get branch-specific solve formats if available;
            # fallback to the native language settings if not.
            branch_solve_format = task.final_format_dict.get(branch_lang, task.final_format_dict.get(lang))
            branch_language_name = task.lang_name_dict.get(branch_lang, branch_lang)
            for start in tqdm(range(0, args.total_dataset_sample, batch_size_cot),
                            desc=f"Math ML for branch {branch_idx+1} ({branch_lang}) for {lang}"):
                batch_prompts = []
                indices = []
                for idx in range(start, min(start+batch_size_cot, args.total_dataset_sample)):
                    # Create a simple step-by-step prompt for this branch.

                    math_ml_solve_prompt = task.math_ml_prompt(
                        source_language=lang,
                        understander_language=branch_lang,
                        shot=args.shot,
                        native_question=native_questions[idx]
                    )

                    messages_cot = [{
                        "role": "user",
                        "content": [{"type": "text", "text": math_ml_solve_prompt}]
                    }]
                    batch_prompts.append(format_chat_prompt(messages_cot))
                    indices.append(idx)
                outputs = safe_generate(batch_prompts, sampling_params, llm, args.model_max_token, tokenizer)
                for i, output in enumerate(outputs):
                    branch_solver_outputs[branch_idx][indices[i]] = output.outputs[0].text

        # Process the outputs: extract predictions for each branch and compute self-consistency vote.
        branch_correct_counts = [0] * num_branches   # Correct count for each branch.
        branch_predictions = [ [None] * args.total_dataset_sample for _ in range(num_branches) ]
        sc_correct_count = 0                         # Self-consistency correct count.
        sc_predictions = [None] * args.total_dataset_sample

        for idx in range(args.total_dataset_sample):
            try:
                ground_truth = task.ground_truth_answer(idx)
                ground_truth_float = float(ground_truth)
            except Exception:
                ground_truth = None
                ground_truth_float = None
            
            # For each branch, extract the final prediction.
            for branch_idx in range(num_branches):
                try:
                    pred = task.extract_final_number(task, branch_solver_outputs[branch_idx][idx])
                except Exception:
                    pred = None
                branch_predictions[branch_idx][idx] = pred
                try:
                    if pred is not None and ground_truth_float is not None:
                        if float(pred) == ground_truth_float:
                            branch_correct_counts[branch_idx] += 1
                except Exception:
                    pass
            
            # Self-consistency voting: vote among the branch solver outputs.
            branch_outputs = [ branch_solver_outputs[b][idx] for b in range(num_branches) ]
            voted_pred = vote_prediction(task, branch_outputs)
            sc_predictions[idx] = voted_pred
            try:
                if voted_pred is not None and ground_truth_float is not None:
                    if float(voted_pred) == ground_truth_float:
                        sc_correct_count += 1
            except Exception:
                pass

        # Compute per-branch and self-consistency accuracies.
        aggregated_branch_accuracies = [count / args.total_dataset_sample for count in branch_correct_counts]
        sc_accuracy = sc_correct_count / args.total_dataset_sample

        # Log results for each question.
        records = []
        for idx in range(args.total_dataset_sample):
            try:
                ground_truth = task.ground_truth_answer(idx)
            except Exception:
                ground_truth = None
            
            # Create a summary string showing all branch predictions and the voted output.
            summary_text = f"Ground Truth: {ground_truth}. "
            for branch_idx in range(num_branches):
                summary_text += f"MathML_{branch_idx+1} prediction: {branch_predictions[branch_idx][idx]}. "
            summary_text += f"Self-consistency MathML voted prediction: {sc_predictions[idx]}."
            
            # Build the record with all required fields.
            record = {
                "question": english_questions[idx],
                "native_question": native_questions[idx],
                "ground_truth": ground_truth,
                "baseline_solver_outputs": { f"MathML_{branch_idx+1}": branch_solver_outputs[branch_idx][idx]
                                            for branch_idx in range(num_branches) },
                "branch_predictions": { f"MathML_{branch_idx+1}": branch_predictions[branch_idx][idx]
                                        for branch_idx in range(num_branches) },
                "self_consistency_prediction": sc_predictions[idx],
                "summary": summary_text,
                "branch_correct_counts": { f"MathML_{branch_idx+1}": branch_correct_counts[branch_idx]
                                        for branch_idx in range(num_branches) },
                "self_consistency_correct_count": sc_correct_count,
                "total_count": args.total_dataset_sample
            }
            records.append(record)
            json_record = json.dumps(record, ensure_ascii=False,
                                    default=lambda o: int(o) if isinstance(o, (np.int64, np.int32)) else o)
            with open(result_json_filename, "a", encoding="utf-8") as fp:
                fp.write(json_record + "\n")
            with open(visual_json_filename, "a", encoding="utf-8") as fp:
                fp.write(json.dumps(record, indent=2, ensure_ascii=False,
                                    default=lambda o: int(o) if isinstance(o, (np.int64, np.int32)) else o) + "\n")
        
        # Report aggregated accuracies.
        print("\n------ MathML Branch Accuracies ------")
        for branch_idx in range(num_branches):
            print(f"Branch {branch_idx+1} ({list_of_languages[branch_idx]}): {aggregated_branch_accuracies[branch_idx]:.2%}")
        print(f"Self-Consistency MathML Accuracy: {sc_accuracy:.2%}\n")



    else:
        # ----- Baseline Chain-of-Thought (CoT) method with multiple branches -----
        print("Using baseline chain-of-thought (CoT) prompt with multiple branches for self-consistency")
        # Use the list of branch languages to determine how many CoT samples to generate.
        list_of_languages = args.understander_lang_list  # e.g., ['en', 'en', 'en']
        list_of_languages = ['en', 'en', 'en']
        num_branches = len(list_of_languages)
        
        # Initialize storage: one output list per branch.
        branch_solver_outputs = [ [None] * args.total_dataset_sample for _ in range(num_branches) ]
        
        batch_size_cot = 25  # Batch size can be adjusted.
        
        # For each branch, generate a solver output using branch-specific prompts.
        for branch_idx, branch_lang in enumerate(list_of_languages):
            # Attempt to get branch-specific solve formats if available;
            # fallback to the native language settings if not.
            branch_solve_format = task.final_format_dict.get(branch_lang, task.final_format_dict.get(lang))
            branch_language_name = task.lang_name_dict.get(branch_lang, branch_lang)
            for start in tqdm(range(0, args.total_dataset_sample, batch_size_cot),
                            desc=f"Baseline CoT for branch {branch_idx+1} ({branch_lang}) for {lang}"):
                batch_prompts = []
                indices = []
                for idx in range(start, min(start+batch_size_cot, args.total_dataset_sample)):
                    # Create a simple step-by-step prompt for this branch.
                    cot_prompt = (
                        f"Solve the following problem in {branch_language_name} step by step. "
                        f"For clarity, you should end with {branch_solve_format}\n"
                        f"{native_questions[idx]}\n"
                        "Answer:"
                    )
                    messages_cot = [{
                        "role": "user",
                        "content": [{"type": "text", "text": cot_prompt}]
                    }]
                    batch_prompts.append(format_chat_prompt(messages_cot))
                    indices.append(idx)
                outputs = llm.generate(batch_prompts, sampling_params)
                for i, output in enumerate(outputs):
                    branch_solver_outputs[branch_idx][indices[i]] = output.outputs[0].text

        # Process the outputs: extract predictions for each branch and compute self-consistency vote.
        branch_correct_counts = [0] * num_branches   # Correct count for each branch.
        branch_predictions = [ [None] * args.total_dataset_sample for _ in range(num_branches) ]
        sc_correct_count = 0                         # Self-consistency correct count.
        sc_predictions = [None] * args.total_dataset_sample

        for idx in range(args.total_dataset_sample):
            try:
                ground_truth = task.ground_truth_answer(idx)
                ground_truth_float = float(ground_truth)
            except Exception:
                ground_truth = None
                ground_truth_float = None
            
            # For each branch, extract the final prediction.
            for branch_idx in range(num_branches):
                try:
                    pred = task.extract_final_number(task, branch_solver_outputs[branch_idx][idx])
                except Exception:
                    pred = None
                branch_predictions[branch_idx][idx] = pred
                try:
                    if pred is not None and ground_truth_float is not None:
                        if float(pred) == ground_truth_float:
                            branch_correct_counts[branch_idx] += 1
                except Exception:
                    pass
            
            # Self-consistency voting: vote among the branch solver outputs.
            branch_outputs = [ branch_solver_outputs[b][idx] for b in range(num_branches) ]
            voted_pred = vote_prediction(task, branch_outputs)
            sc_predictions[idx] = voted_pred
            try:
                if voted_pred is not None and ground_truth_float is not None:
                    if float(voted_pred) == ground_truth_float:
                        sc_correct_count += 1
            except Exception:
                pass

        # Compute per-branch and self-consistency accuracies.
        aggregated_branch_accuracies = [count / args.total_dataset_sample for count in branch_correct_counts]
        sc_accuracy = sc_correct_count / args.total_dataset_sample

        # Log results for each question.
        records = []
        for idx in range(args.total_dataset_sample):
            try:
                ground_truth = task.ground_truth_answer(idx)
            except Exception:
                ground_truth = None
            
            # Create a summary string showing all branch predictions and the voted output.
            summary_text = f"Ground Truth: {ground_truth}. "
            for branch_idx in range(num_branches):
                summary_text += f"Cot_{branch_idx+1} prediction: {branch_predictions[branch_idx][idx]}. "
            summary_text += f"Self-consistency voted prediction: {sc_predictions[idx]}."
            
            # Build the record with all required fields.
            record = {
                "question": english_questions[idx],
                "native_question": native_questions[idx],
                "ground_truth": ground_truth,
                "baseline_solver_outputs": { f"cot_{branch_idx+1}": branch_solver_outputs[branch_idx][idx]
                                            for branch_idx in range(num_branches) },
                "branch_predictions": { f"cot_{branch_idx+1}": branch_predictions[branch_idx][idx]
                                        for branch_idx in range(num_branches) },
                "self_consistency_prediction": sc_predictions[idx],
                "summary": summary_text,
                "branch_correct_counts": { f"cot_{branch_idx+1}": branch_correct_counts[branch_idx]
                                        for branch_idx in range(num_branches) },
                "self_consistency_correct_count": sc_correct_count,
                "total_count": args.total_dataset_sample
            }
            records.append(record)
            json_record = json.dumps(record, ensure_ascii=False,
                                    default=lambda o: int(o) if isinstance(o, (np.int64, np.int32)) else o)
            with open(result_json_filename, "a", encoding="utf-8") as fp:
                fp.write(json_record + "\n")
            with open(visual_json_filename, "a", encoding="utf-8") as fp:
                fp.write(json.dumps(record, indent=2, ensure_ascii=False,
                                    default=lambda o: int(o) if isinstance(o, (np.int64, np.int32)) else o) + "\n")
        
        # Report aggregated accuracies.
        print("\n------ Baseline CoT Branch Accuracies ------")
        for branch_idx in range(num_branches):
            print(f"Branch {branch_idx+1} ({list_of_languages[branch_idx]}): {aggregated_branch_accuracies[branch_idx]:.2%}")
        print(f"Self-Consistency CoT Accuracy: {sc_accuracy:.2%}\n")