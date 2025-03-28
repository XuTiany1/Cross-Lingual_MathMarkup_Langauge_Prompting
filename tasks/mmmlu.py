import re
import os
import sympy
import pandas as pd
from tasks.task import Task, DATA_PATH
import importlib
import math
from datasets import load_dataset
from prompts.MMMLU.EN import *
import csv



class mmlu_task(Task):

    def __init__(self, args):
        super().__init__()

        gmmlu_data_card = "CohereForAI/Global-MMLU"
        gmmlu_data_dir = "data/global_mmlu/"
        os.makedirs(gmmlu_data_dir, exist_ok=True)
        mmmlu_lang = ['en', 'es', 'fr']

        # Download the dataset in JSON Lines format
        self.download_dataset(gmmlu_data_card, gmmlu_data_dir, mmmlu_lang)

        # Load the chosen language dataset
        chosen_lang = args.lang
        lang_dir = os.path.join(gmmlu_data_dir, chosen_lang)
        print("Language directory:", lang_dir)

        # Point to JSONL files instead of TSV
        dev_file = os.path.join(lang_dir, "dev.jsonl")
        test_file = os.path.join(lang_dir, "test.jsonl")

        # Read the JSON Lines with Pandas
        self.dev_data = pd.read_json(dev_file, orient="records", lines=True)
        self.test_data = pd.read_json(test_file, orient="records", lines=True)

        # By default, use test_data as the active data
        self.data = self.test_data

        # Also load English test data for reference
        en_lang_dir = os.path.join(gmmlu_data_dir, "en")
        en_test_file = os.path.join(en_lang_dir, "test.jsonl")
        self.english_data = pd.read_json(en_test_file, orient="records", lines=True)




    #################
    # Dataset Download
    #################
    def download_dataset(self, data_card, data_dir, list_of_languages):

        for lang in list_of_languages:
            lang_dir = os.path.join(data_dir, lang)
            dev_file = os.path.join(lang_dir, "dev.jsonl")
            test_file = os.path.join(lang_dir, "test.jsonl")

            # Skip downloading if files already exist
            if os.path.exists(dev_file) and os.path.exists(test_file):
                print(f"Dataset for {lang} already exists. Skipping download.")
                continue

            print(f"Downloading dataset for language: {lang}")
            dataset = load_dataset(data_card, lang)
            os.makedirs(lang_dir, exist_ok=True)

            # Save train and test splits as JSON Lines
            dataset["test"].to_json(
                test_file,
                orient="records",
                lines=True,
                force_ascii=False
            )
            dataset["dev"].to_json(
                dev_file,
                orient="records",
                lines=True,
                force_ascii=False
            )




    def __len__(self) -> int:
        """
        Returns the number of data instances in the current split.
        """
        return len(self.data)


    def get_input(self, idx: int) -> str:
        """
        Returns the question (input) at the given index in the current split.
        """
        if idx < 0 or idx >= len(self.data):
            raise IndexError("Index out of range.")
        
        return self.data.iloc[idx]["question"]
    

    def get_choices(self, idx: int) -> str:
        """
        Returns the question (input) at the given index in the current split.
        """
        if idx < 0 or idx >= len(self.data):
            raise IndexError("Index out of range.")
        
        option_a = self.data.iloc[idx]["option_a"]
        option_b = self.data.iloc[idx]["option_b"]
        option_c = self.data.iloc[idx]["option_c"]
        option_d = self.data.iloc[idx]["option_d"]
        
        list_of_choices = [option_a, option_b, option_c, option_d]

        return list_of_choices
    

    def get_subject_category(self, idx: int) -> list:

        subject = self.data.iloc[idx]["subject"]
        category = self.data.iloc[idx]["subject_category"]

        return [category, subject]
        



    def get_english_input(self, idx: int) -> str:
        """
        Returns the question (input) at the given index in the current split.
        """
        if idx < 0 or idx >= len(self.data):
            raise IndexError("Index out of range.")
        
        return self.english_data.iloc[idx]["question"]


    def ground_truth_answer(self, idx: int):
        """
        output answer
        """
        return self.data.iloc[idx]["answer"]
    

    @staticmethod
    def prompt_wrap(self,
                    question: str,
                    lang: str,
                    subject: str,
                    list_of_choices: list) -> str:

        prompt = cot_prompt_2.format(
            subject = subject,
            question = question,
            choice1 = list_of_choices[0],
            choice2 = list_of_choices[1],
            choice3 = list_of_choices[2],
            choice4 = list_of_choices[3]
        )

        return prompt



    ############
    # Extract the final answer
    ############
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




