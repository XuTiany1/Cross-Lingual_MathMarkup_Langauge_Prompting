import os
from huggingface_hub import snapshot_download
from vllm import LLM, SamplingParams
import argparse

# ===================================================================
# Define arguments
args = argparse.Namespace(
    task='MATH',
    lang='en',  # Default, will be overwritten in the loop
    languages=['zh', 'es', 'ru'], 
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
snapshot_download(
    repo_id="lightblue/DeepSeek-R1-Distill-Qwen-7B-Multilingual", 
    local_dir=args.local_model_path
)

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



# Define your prompt.
prompts = [
    """学校には1クラスにつき20人の生徒がおり、クラスは合計3つあります。
学校全体では男子と女子がそれぞれ50%ずついます。
1つ目のクラスには女子が15人、2つ目のクラスには女子が12人います。
3つ目のクラスには何人の男子がいますか？"""
]

# Format the conversation as expected by vllm.
conversations = [
    [{"role": "user", "content": prompt}] for prompt in prompts
]

# Run the chat with the model.
outputs = llm.chat(conversations, sampling_params=sampling_params)

# Print the output.
for output in outputs:
    print(output.outputs[0].text)
