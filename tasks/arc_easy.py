import re
import os
import sympy
import pandas as pd
from tasks.task import Task, DATA_PATH
import importlib
import math
from datasets import load_dataset
from prompts.ARC.arc_prompt import *
import csv



class arc_easy(Task):

    def __init__(self, args):
        super().__init__()


        lang_to_datasource_dict = {
            "amh": "masakhane/uhura-arc-easy",
            "ha": "masakhane/uhura-arc-easy",
            "en": "masakhane/uhura-arc-easy",
            "nso": "masakhane/uhura-arc-easy",
            "sw": "masakhane/uhura-arc-easy",
            "yo": "masakhane/uhura-arc-easy",
            "zu": "masakhane/uhura-arc-easy",
            "te": "Cognitive-Lab/Indic-ARC-Easy",
            "ml": "Thanmay/arc-easy-ml",
            "ta": "Thanmay/arc-easy-ta",
            "mr": "Thanmay/arc-easy-mr",
            "hi": "Thanmay/arc-easy-hi"
        }

        arc_easy_data_dir = "data/arc_easy/"
        os.makedirs(arc_easy_data_dir, exist_ok=True)
        arc_easy_lang = ['amh', 'ha', 'en', 'nso' , 'sw', 'yo', 'zu', 'ml', 'ta', 'mr', 'hi']

        # Download the dataset in JSON Lines format
        self.download_dataset(lang_to_datasource_dict, arc_easy_data_dir, arc_easy_lang)

        # Load the chosen language dataset
        chosen_lang = args.lang
        lang_dir = os.path.join(arc_easy_data_dir, chosen_lang)
        print("Language directory:", lang_dir)

        # Point to JSONL files instead of TSV
        test_file = os.path.join(lang_dir, "test.jsonl")

        # Read the JSON Lines with Pandas
        self.test_data = pd.read_json(test_file, orient="records", lines=True)

        # By default, use test_data as the active data
        self.data = self.test_data

        # Also load English test data for reference
        en_lang_dir = os.path.join(arc_easy_data_dir, "en")
        en_test_file = os.path.join(en_lang_dir, "test.jsonl")
        self.english_data = pd.read_json(en_test_file, orient="records", lines=True)


    #################
    # Dataset Download
    #################

    def download_dataset(self, lang_to_datasource_dict, data_dir, list_of_languages):

        for lang, datasource in lang_to_datasource_dict.items():
            if lang not in list_of_languages:
                continue  # Skip languages not in the list

            lang_dir = os.path.join(data_dir, lang)
            os.makedirs(lang_dir, exist_ok=True)
            output_file = os.path.join(lang_dir, "test.jsonl")

            # Skip if file already exists
            if os.path.exists(output_file):
                print(f"Dataset for {lang} already exists. Skipping download.")
                continue

            print(f"Downloading dataset for language: {lang}")


            # Determine the configuration and split based on the language
            if lang in ["amh", "ha", "en", "nso", "sw", "yo", "zu"]:
                # Use specific builder configs for amh and ha
                lang_to_config_name = {
                    "amh": "am_multiple_choice",
                    "ha": "ha_multiple_choice",
                    "en": "en_multiple_choice",
                    "nso": "nso_multiple_choice",
                    "sw": "sw_multiple_choice",
                    "yo": "yo_multiple_choice",
                    "zu": "zu_multiple_choice"
                }
                config = lang_to_config_name[lang]
                split = "test"
                dataset = load_dataset(datasource, config)
                dataset[split].to_json(
                    output_file,
                    orient="records",
                    lines=True,
                    force_ascii=False
                )
            elif lang in ["ml", "ta", "mr", "hi"]:
                split = "validation"
                dataset = load_dataset(datasource)
                dataset[split].to_json(
                    output_file,
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
        
        choices_dict = self.data.iloc[idx]["choices"]
        
        return choices_dict["text"]
        



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
        return self.data.iloc[idx]["answerKey"]
    

    #############
    # Prompting methods
    #############
    @staticmethod
    def ds_native_prompt_wrap(self,
                              question: str,
                              lang: str,
                              list_of_choices: list) -> str:

        prompt = ds_native_language_prompt.format(
            question = question,
            choice1 = list_of_choices[0],
            choice2 = list_of_choices[1],
            choice3 = list_of_choices[2],
            choice4 = list_of_choices[3]
        )

        return prompt

    @staticmethod
    def ds_english_prompt_wrap(self,
                              question: str,
                              lang: str,
                              list_of_choices: list) -> str:

        prompt = ds_native_language_prompt.format(
            question = question,
            choice1 = list_of_choices[0],
            choice2 = list_of_choices[1],
            choice3 = list_of_choices[2],
            choice4 = list_of_choices[3]
        )

        return prompt

    @staticmethod
    def qw_native_prompt_wrap(self,
                              question: str,
                              lang: str,
                              list_of_choices: list) -> str:

        prompt = qw_native_language_prompt.format(
            question = question,
            choice1 = list_of_choices[0],
            choice2 = list_of_choices[1],
            choice3 = list_of_choices[2],
            choice4 = list_of_choices[3]
        )

        return prompt

    @staticmethod
    def qw_english_prompt_wrap(self,
                              question: str,
                              lang: str,
                              list_of_choices: list) -> str:

        prompt =qw_native_language_prompt.format(
            question = question,
            choice1 = list_of_choices[0],
            choice2 = list_of_choices[1],
            choice3 = list_of_choices[2],
            choice4 = list_of_choices[3]
        )

        return prompt
    

    @staticmethod
    def qwc_native_prompt_wrap(self,
                              question: str,
                              lang: str,
                              list_of_choices: list) -> str:

        prompt = qwc_native_language_prompt.format(
            question = question,
            choice1 = list_of_choices[0],
            choice2 = list_of_choices[1],
            choice3 = list_of_choices[2],
            choice4 = list_of_choices[3]
        )

        return prompt

    @staticmethod
    def qwc_english_prompt_wrap(self,
                              question: str,
                              lang: str,
                              list_of_choices: list) -> str:

        prompt =qwc_native_language_prompt.format(
            question = question,
            choice1 = list_of_choices[0],
            choice2 = list_of_choices[1],
            choice3 = list_of_choices[2],
            choice4 = list_of_choices[3]
        )

        return prompt



    ############
    # Extract the final answer from multichoice
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




