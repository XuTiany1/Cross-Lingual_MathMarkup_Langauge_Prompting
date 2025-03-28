import json
import re


@staticmethod
def extract_final_answer(response: str):
    # List of regex patterns for common answer formats.
    patterns = [
        r'Answer\s+is\s+([ABCD])\s*$',             # Matches "Answer is A" (at end of string)
        r'Answer:\s*([ABCD])\s*$',                  # Matches "Answer: A"
        r'Answer\s*should\s*be\s*([ABCD])\s*$',       # Matches "Answer should be A"
        r'Final\s+Answer\s*[:=]?\s*([ABCD])\s*$',     # Matches "Final Answer: A" or "Final Answer = A"
    ]
    # Try each pattern in order.
    for pattern in patterns:
        match = re.search(pattern, response, re.IGNORECASE)
        if match:
            return match.group(1).upper()
    
    # Fallback: capture the last standalone capitalized letter A, B, C, or D.
    letters = re.findall(r'\b([ABCD])\b', response)
    if letters:
        return letters[-1].upper()
    
    return None

def debug_extraction(input_file, output_file):
    """
    Reads the input JSONL file, applies the extraction to each entry,
    and writes a new JSONL file that includes the extracted answer and a flag indicating correctness.
    """
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            data = json.loads(line)
            # Extract the answer from the 'model_reasoning' field.
            extracted = extract_final_answer(data["model_reasoning"])
            data["extracted_answer"] = extracted
            # Optionally compare the extracted answer with the ground truth.
            data["extraction_correct"] = (extracted == data.get("ground_truth"))
            outfile.write(json.dumps(data) + "\n")


if __name__ == "__main__":
    input_path = "/home/mila/x/xut/github/multilingual_deepseek/multilingual_mmlu_result/en/en_result.jsonl"
    output_path = "debug_extraction_results.jsonl"
    debug_extraction(input_path, output_path)
    print(f"Extraction debugging complete. Results written to {output_path}")

