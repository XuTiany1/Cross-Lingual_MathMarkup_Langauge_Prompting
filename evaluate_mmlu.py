import os
import argparse
import evaluate
import json
from huggingface_hub import snapshot_download
from vllm import LLM, SamplingParams
from tasks.mmmlu import mmlu_task

# ===================================================================
# Define arguments

args = argparse.Namespace(
    task='MMLU',
    lang='en',  # Default, will be overwritten in the loop
    languages=['en'], 
    local_model_path='/home/mila/x/xut/scratch/model/multilingual_reasoning',
    model_max_token=8000,
    model_temperature=0.5,
    total_dataset_sample=250
)



# ===================================================================
# Set up folder
os.makedirs(args.local_model_path, exist_ok=True)

# ===================================================================
# Download model to local repo

if not os.listdir(args.local_model_path):
    # Download model to local repo if not already present
    snapshot_download(
        repo_id="lightblue/DeepSeek-R1-Distill-Qwen-7B-Multilingual", 
        local_dir=args.local_model_path
    )
else:
    print("Model already exists, skipping download.")

# ===================================================================
# Initialize the model from the local directory.
llm = LLM(
    model=args.local_model_path,
    max_model_len=args.model_max_token
)

sampling_params = SamplingParams(
    temperature=args.model_temperature, 
    max_tokens=args.model_max_token
)

# ===================================================================
# Set up Variables
run_folder = os.path.join("multilingual_mmlu_result")
os.makedirs(run_folder, exist_ok=True)
exact_match_metric = evaluate.load("accuracy")

# ===================================================================
# Main Loop: Process each language in batch
for lang in args.languages:
    total_count = 0
    correct_count = 0
    model_preds = []
    ground_truth_refs = []
    error_questions = []

    args.lang = lang
    task = mmlu_task(args)
    lang_dir_path = os.path.join("multilingual_mmlu_result", f"{lang}")
    os.makedirs(lang_dir_path, exist_ok=True)


    # Prepare hyperparameter log
    hyperparams_path = os.path.join(lang_dir_path, f"{lang}-hyperparams.log")
    with open(hyperparams_path, "w") as hp:
        hp.write("--- Hyperparameters / Args ---\n")
        for k, v in vars(args).items():
            hp.write(f"{k}: {v}\n")

    # JSON Lines files to store results
    json_filename = os.path.join(lang_dir_path, f"{lang}_result.jsonl")
    os.makedirs(os.path.dirname(json_filename), exist_ok=True)

    good_looking_json_filename = os.path.join(lang_dir_path, f"{lang}_good_looking_result.jsonl")
    os.makedirs(os.path.dirname(good_looking_json_filename), exist_ok=True)

    # -------------------------------------------------------------------
    # Collect prompts and metadata for batching
    batch_prompts = []
    batch_native_questions = []
    batch_english_questions = []
    batch_indices = []
    
    answer_to_int = {'A': 0, 'B': 1, 'C': 2, 'D': 3}



    # args.total_dataset_sample
    total_sample = task.__len__()
    for idx in range(1, total_sample):
        total_count += 1
        print(f"\n--- Collecting Test {idx} for language {lang} ---")
        native_question = task.get_input(idx)
        english_question = task.get_english_input(idx)
        list_of_choices = task.get_choices(idx)
        category = task.get_subject_category(idx)

        
        prompt = task.prompt_wrap(task, 
                                  native_question, 
                                  lang,
                                  category[1],
                                  list_of_choices
                                  )
        
        batch_prompts.append(prompt)
        batch_native_questions.append(native_question)
        batch_english_questions.append(english_question)
        batch_indices.append(idx)

    # -------------------------------------------------------------------
    # Create batched conversations for vllm (each prompt is independent)
    conversations = [[{"role": "user", "content": prompt}] for prompt in batch_prompts]
    
    # Run the chat on the full batch
    outputs = llm.chat(conversations, sampling_params=sampling_params)

    # -------------------------------------------------------------------
    # Process each batched output
    for i, output in enumerate(outputs):
        output_str = output.outputs[0].text  # Extract model output string
        

        print (output_str)


        try:
            model_answer = task.extract_final_answer(output_str)
        except ValueError as e:
            print(f"Error for test {batch_indices[i]}: {e}")
            model_answer = None

        # Ground Truth extraction
        try:
            ground_truth_answer = task.ground_truth_answer(batch_indices[i])
        except ValueError as e:
            print(f"Error converting ground truth for test {batch_indices[i]}: {e}")
            error_questions.append(batch_english_questions[i])

        # Accuracy check
        is_correct = (
            model_answer is not None and
            ground_truth_answer is not None and
            model_answer == ground_truth_answer
        )

        if is_correct:
            correct_count += 1
        model_accuracy = correct_count / total_count

        # Update metrics for Huggingface exact match metric
        model_preds.append(model_answer)
        ground_truth_refs.append(ground_truth_answer)

        predictions_int = [answer_to_int[a] if a is not None else -1 for a in model_preds]
        references_int = [answer_to_int[a] for a in ground_truth_refs]

        current_ac_model = exact_match_metric.compute(
            predictions=predictions_int, references=references_int
        )["accuracy"]

        # Prepare the record for logging
        record = {
            "question": str(batch_english_questions[i]),
            "native_question": str(batch_native_questions[i]),
            "choice a, b, c, d" : list_of_choices,
            "model_answer": model_answer,
            "ground_truth": ground_truth_answer,
            "model_reasoning": str(output_str),
            "model_accuracy_hand_calculated": float(model_accuracy),
            "model_accuracy_huggingface": f"{current_ac_model:.2%}",
        }

        # Save record to JSON Lines file
        with open(json_filename, "a", encoding="utf-8") as fp:
            fp.write(json.dumps(record, ensure_ascii=False) + "\n")

        with open(good_looking_json_filename, "a", encoding="utf-8") as fp:
            fp.write(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
