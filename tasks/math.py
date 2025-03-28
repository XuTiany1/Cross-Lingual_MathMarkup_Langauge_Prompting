import re
import os
import sympy
import pandas as pd
from tasks.task import Task, DATA_PATH
import importlib
import math
from datasets import load_dataset


class math_task(Task):

    def __init__(self, args):

        super().__init__()

        ################################
        # Download dataset 
        # First, downlaoad AFRI_MGSM
        afri_data_card = "masakhane/afrimgsm"
        afri_data_dir = "data/AFRI_MGSM/"
        os.makedirs(afri_data_dir, exist_ok=True)
        afri_mgsm_lang = ['amh', 'ewe', 'hau', 'ibo', 'kin', 'lin', 'lug', 'orm', 'sna', 'sot', 'swa', 'twi', 'vai', 'wol', 'xho', 'yor', 'zul']
        self.download_dataset(afri_data_card, afri_data_dir, afri_mgsm_lang)


        mgsm_data_card = "juletxara/mgsm"
        mgsm_data_dir = "data/MGSM/"
        os.makedirs(mgsm_data_dir, exist_ok=True)
        mgsm_lang = ['en', 'es', 'fr', 'de', 'ru', 'zh', 'ja', 'th', 'sw', 'bn', 'te']
        self.download_dataset(mgsm_data_card, mgsm_data_dir, mgsm_lang)

        # Load the chosen langauge dataset
        chosen_lang = args.lang
        
        if chosen_lang in afri_mgsm_lang:
            lang_dir = os.path.join(afri_data_dir, chosen_lang)
        else:
            lang_dir = os.path.join(mgsm_data_dir, chosen_lang)
        print(lang_dir)
        train_file = os.path.join(lang_dir, "train.tsv")
        test_file = os.path.join(lang_dir, "test.tsv")

        self.train_data = pd.read_csv(train_file, sep="\t", quoting=3)
        self.test_data = pd.read_csv(test_file, sep="\t", quoting=3)

        # Set current data into either train or test
        self.data = self.test_data

        ################################
        # English dataset
        en_lang_dir = os.path.join(mgsm_data_dir, 'en')
        en_test_file = os.path.join(en_lang_dir, "test.tsv")
        self.english_data = pd.read_csv(en_test_file, sep="\t", quoting=3)
        
        ################################
        # Language Dictionary
        self.lang_dic = {
            # mgsm_lang
            'en': "Solve and make sure the last number is the final answer:",
            'es': "Resuelve:",
            'fr': "Résous:",
            'de': "Löse, Die letzte Zahl sollte die endgültige Antwort sein:",
            'ru': "решить проблему:",
            'zh': "解答, 最后一个数字应该是最终答案。：",
            'ja': "解いてください：",
            'th': "แก้:",
            'sw': "Tatua:",
            'bn': "সমাধান করুন:",
            'te': "పరిష్కరించండి:",
        }



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
            dataset["train"].to_pandas().to_csv(os.path.join(lang_dir, "train.tsv"), sep="\t", index=False)
            dataset["test"].to_pandas().to_csv(os.path.join(lang_dir, "test.tsv"), sep="\t", index=False)



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
        return self.data.iloc[idx]["answer_number"]
    

    @staticmethod
    def prompt_wrap(self,
                    question: str,
                    lang: str) -> str:
        
        language_solve = self.lang_dic.get(lang, "Solve:")  # Default to English if language not found

        prompt = f"{language_solve}: {question}"

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
        print(final_number_str)
        try:
            num = float(final_number_str)
            if math.isinf(num):
                return 0  # or handle the case as needed
            return int(num)

        except ValueError:
            return 0








