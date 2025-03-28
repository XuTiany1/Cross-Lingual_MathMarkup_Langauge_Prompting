import re
import os
import sympy
import pandas as pd
import csv
import math
from tasks.task import Task, DATA_PATH
from datasets import load_dataset
from prompts.MMMLU.EN import *

class mmlu_task(Task):

    def __init__(self, args):
        super().__init__()

        ################################
        # Download dataset 
        # First, download AFRI_MGSM
        mmmlu_data_card = "alexandrainst/m_mmlu"
        mmmlu_data_dir = "data/m_mmlu/"
        os.makedirs(mmmlu_data_dir, exist_ok=True)
        # 'ar', 'bn', 'ca', 'da', 'de', 'en', 'es', 'eu','fr', 'gu', 'hi', 'hr', 'hu', 'hy', 'id', 'is', 'kn', 'ml', 'mr', 'nb', 'ne', 'nl'
        mmmlu_lang = ['en', 'es', 'fr']
        self.download_dataset(mmmlu_data_card, mmmlu_data_dir, mmmlu_lang)

        # Load the chosen language dataset
        chosen_lang = args.lang
        lang_dir = os.path.join(mmmlu_data_dir, chosen_lang)
        print("Language directory:", lang_dir)

        train_file = os.path.join(lang_dir, "train.tsv")
        test_file = os.path.join(lang_dir, "test.tsv")

        self.train_data = pd.read_csv(train_file, sep='\t', engine='python', quoting=csv.QUOTE_NONE)
        self.test_data = pd.read_csv(test_file, sep='\t', engine='python', quoting=csv.QUOTE_NONE)

        # Set current data into either train or test
        self.data = self.test_data

        ################################
        # English dataset
        en_lang_dir = os.path.join(mmmlu_data_dir, 'en')
        en_test_file = os.path.join(en_lang_dir, "test.tsv")
        self.english_data = pd.read_csv(en_test_file, sep="\t", quoting=3)

    #################
    # Dataset Download
    #################
    def download_dataset(self, data_card, data_dir, list_of_languages):
        # Download and save datasets for each language
        for lang in list_of_languages:
            lang_dir = os.path.join(data_dir, lang)
            train_file = os.path.join(lang_dir, "train.tsv")
            test_file = os.path.join(lang_dir, "test.tsv")

            # Skip downloading if files already exist
            if os.path.exists(train_file) and os.path.exists(test_file):
                print(f"Dataset for {lang} already exists. Skipping download.")
                continue  # Skip to next language

            print(f"Downloading dataset for language: {lang}")
            dataset = load_dataset(data_card, lang)
            os.makedirs(lang_dir, exist_ok=True)

            # Save train and test splits as TSV files
            dataset["train"].to_pandas().to_csv(train_file, sep="\t", index=False)
            dataset["test"].to_pandas().to_csv(test_file, sep="\t", index=False)

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
        return self.data.iloc[idx]["instruction"]

    def get_english_input(self, idx: int) -> str:
        """
        Returns the question (input) at the given index in the English dataset.
        """
        if idx < 0 or idx >= len(self.english_data):
            raise IndexError("Index out of range.")
        return self.english_data.iloc[idx]["instruction"]

    def ground_truth_answer(self, idx: int):
        """
        Returns the answer at the given index in the current split.
        """
        return self.data.iloc[idx]["answer"]

    @staticmethod
    def prompt_wrap(self, question: str, lang: str, subject: str, list_of_choices: list) -> str:
        prompt = cot_prompt_2.format(
            subject=subject,
            question=question,
            choice1=list_of_choices[0],
            choice2=list_of_choices[1],
            choice3=list_of_choices[2],
            choice4=list_of_choices[3]
        )
        return prompt

    ############
    # Extract the final answer
    ############
    @staticmethod
    def extract_final_number(self, response: str):
        """
        Extracts the final numerical value from the response string.
        This function looks for numbers that may include commas, a dollar sign,
        a sign (+/-), and an optional decimal part.
        
        If a number is found, it returns it as an int or float.
        If no number is found, it returns 0.
        """
        # This regex pattern matches:
        # - An optional sign (- or +)
        # - An optional dollar sign ($)
        # - A digit (with possible commas in the middle)
        # - An optional decimal part
        pattern = re.compile(r'[-+]?\$?\d[\d,]*(?:\.\d+)?')
        matches = pattern.findall(response)
        
        if not matches:
            return 0

        # Grab the last match
        final_number_str = matches[-1]
        
        # Remove common extraneous symbols like '$' and commas
        final_number_str = final_number_str.replace('$', '').replace(',', '')
        print("Extracted string:", final_number_str)
        try:
            num = float(final_number_str)
            if math.isinf(num):
                return 0  # or handle the case as needed
            return int(num)
        except ValueError:
            return 0

if __name__ == "__main__":
    import argparse

    # Set up argument parsing for debugging
    parser = argparse.ArgumentParser(description="Debug mmlu_task")
    parser.add_argument("--lang", type=str, default="en", help="Language code (e.g., en, es, fr)")
    args = parser.parse_args()

    # Instantiate the task
    task = mmlu_task(args)

    # Print basic info from the datasets
    print("\nTrain data shape:", task.train_data.shape)
    print("Test data shape:", task.test_data.shape)
    print("English data shape:", task.english_data.shape)

    # Display a preview of the train and test datasets
    print("\nFirst few rows of train data:")
    print(task.train_data.head())

    print("\nFirst few rows of test data:")
    print(task.test_data.head())

    print("\nFirst few rows of English data:")
    print(task.english_data.head())

    # Test the get_input and ground_truth_answer methods
    try:
        first_instruction = task.get_input(0)
        first_ground_truth = task.ground_truth_answer(0)
        print("\nFirst instruction from test data:")
        print(first_instruction)
        print("Ground truth answer for first test example:")
        print(first_ground_truth)
    except Exception as e:
        print("Error while retrieving test data:", e)

    # Test the get_english_input method
    try:
        english_instruction = task.get_english_input(0)
        print("\nFirst instruction from English data:")
        print(english_instruction)
    except Exception as e:
        print("Error while retrieving English data:", e)

    # Test the static method extract_final_number with a sample response
    sample_response = "The final result is 3,141.59 dollars."
    extracted_number = mmlu_task.extract_final_number(None, sample_response)
    print("\nExtracted number from sample response:", extracted_number)
