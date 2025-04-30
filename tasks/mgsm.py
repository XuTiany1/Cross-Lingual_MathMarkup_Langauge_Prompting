import re
import os
import sympy
import pandas as pd
from tasks.task import Task, DATA_PATH
import importlib
import math
from datasets import load_dataset
from prompts.MGSM.math_prompt import *
from prompts.MGSM.pal_examplar import *
from prompts.MGSM.clp_examplar import *
from prompts.MGSM.mathml_examplar import *


class mgsm(Task):

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

        #################################
        # fuinal formatting dictionary
        self.final_format_dict = {
            "zh": "答案是：[数字]。",
            "bn": "উত্তর হল: [num]",
            "de": "Die Antwort ist: [num]",
            "es": "La respuesta es: [num]",
            "fr": "La réponse est : [num]",
            "ja": "答えは：[数字]。",
            "ru": "Ответ: [num]",
            "sw": "Jibu ni: [num]",
            "te": "సమాధానం: [num]",
            "th": "คำตอบคือ: [num]",
            "en": "The answer is: [num]",
            "amh": "መልስ ነው: [num]",
            "ewe": "Ŋuɖoɖoa nye: [num]",
            "hau": "Amsa ita ce: [num]",
            "ibo": "Azịza bụ: [num]",
            "kin": "Igisubizo ni: [num]",
            "yor": "Idahun si jẹ: [num]",
            "zul": "Impendulo ithi: [num]",
            "lin": "Eyano na yango: [num]",
            "sot": "Karabo ke gore: [num]",
            "sna": "Mhinduro ndeyekuti: [num]",
            "lug": "Eky’okuddamu kiri nti: [num]",
            "hau": "Amsar ita ce: [num]",
            "orm": "Deebiin isaa: [num]",
            "twi": "mmuae no ne sɛ: [num]",
            "wol": "tontu li mooy: [num]",
            "xho": "Impendulo ithi: [num]",
            "vai": "tꔂ ꕉnsꔃr ꔤs: [num]"
            
        }

        #################################
        # Set up language name dictionary for better prompting
        self.lang_name_dict = {
            "zh": "chinese",
            "bn": "bengali",
            "de": "german",
            "es": "spanish",
            "fr": "french",
            "ja": "japanese",
            "ru": "russian",
            "sw": "swahili",
            "te": "telugu",
            "th": "thai",
            "en": "english",
            "amh": "amheric",
            "ewe": "ewe",
            "hau": "hausa",
            "ibo": "igbo",
            "kin": "kinyarwanda",
            "yor": "yoruba",
            "zul": "zulu",
            "lin": "lingala",
            "sot": "tswana",
            "sna": "shona",
            "lug": "luganda",
            "hau": "hausa",
            "orm": "oromo",
            "twi": "Akan",
            "wol": "Wolof",
            "xho": "Xhosa",
            "vai": "vai"
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
    

    def get_langauge_name(self, source_language:int):
        return self.lang_name_dict.get(source_language) 




    ################################
    # Prompt calling
    def ds_prompt_wrap(self,
                       native_question: str, 
                       source_lang: str) -> str:
        
        prompt_name = f"ds_{source_lang}_prompt"

        if prompt_name not in globals():
            raise ValueError(f"No prompt found for language: {source_lang}")

        prompt_template = globals()[prompt_name]

        return prompt_template.format(question=native_question)


    # COT prompt wrap
    def cot_prompt_wrap(self,
                       native_question: str, 
                       source_lang: str) -> str:
        
        prompt_name = f"cot_{source_lang}_prompt"

        if prompt_name not in globals():
            raise ValueError(f"No prompt found for language: {source_lang}")

        prompt_template = globals()[prompt_name]

        return prompt_template.format(question=native_question)


    # Understander prompt format
    def understand_prompt(self,
                        source_language: str,
                        understander_language: str,
                        shot: int,
                        native_question: str) -> str:
        
        # Build the variable name
        list_name = f"{source_language}_example_list"
        
        # Check if that variable exists in globals
        if list_name not in globals():
            raise ValueError(f"No examples found for language: {source_language}")
        
        # Retrieve the list of examples
        examples_list = globals()[list_name]
        
        # Ensure the requested shot does not exceed available examples
        if shot > len(examples_list):
            shot = len(examples_list)
        
        # Concatenate the selected examples into one string
        examples = "\n".join(examples_list[:shot])

        # Find the language name for better prompting
        source_language_name = self.lang_name_dict.get(source_language) 
        understand_language_name = self.lang_name_dict.get(understander_language)
        
        # Format the prompt using your understand_prompt template
        prompt = understand_prompt.format(source_language=source_language_name,
                                        examples=examples,
                                        native_question=native_question,
                                        understander_language=understand_language_name)
        return prompt
    
    # Understander prompt format
    def clp_understand_prompt(self,
                        source_language: str,
                        understander_language: str,
                        shot: int,
                        native_question: str) -> str:
        
        # Build the variable name
        clp_list_name = f"clp_{source_language}_example_list"
        
        # Check if that variable exists in globals
        if clp_list_name not in globals():
            raise ValueError(f"No examples found for language: {source_language}")
        
        # Retrieve the list of examples
        examples_list = globals()[clp_list_name]
        
        # Ensure the requested shot does not exceed available examples
        if shot > len(examples_list):
            shot = len(examples_list)
        
        # Concatenate the selected examples into one string
        examples = "\n".join(examples_list[:shot])

        # Find the language name for better prompting
        source_language_name = self.lang_name_dict.get(source_language) 
        understand_language_name = self.lang_name_dict.get(understander_language)

        mathml_examples = '''
            Examplar 1:
            MathML: 
            <math xmlns="http://www.w3.org/1998/Math/MathML">
            <mrow>
                <mn>5</mn>
                <mo>+</mo>
                <mn>2</mn>
                <mo>&#x00D7;</mo>
                <mn>3</mn>
                <mo>=</mo>
                <mn>11</mn>
            </mrow>
            </math>
        '''
        
        # Format the prompt using your understand_prompt template
        prompt = clp_understand_prompt.format(source_language=source_language_name,
                                        examples=examples,
                                        mathml_examples=mathml_examples,
                                        native_question=native_question,
                                        understander_language=understand_language_name)
        return prompt


    # Understander prompt format
    def mathML_understand_prompt(self,
                        source_language: str,
                        understander_language: str,
                        shot: int,
                        native_question: str) -> str:
        
        # Build the variable name
        math_ml_list_name = f"ml_example_list"
        
        # Check if that variable exists in globals
        if math_ml_list_name not in globals():
            raise ValueError(f"No examples found for language: {source_language}")
        
        # Retrieve the list of examples
        examples_list = globals()[math_ml_list_name]
        
        # Ensure the requested shot does not exceed available examples
        if shot > len(examples_list):
            shot = len(examples_list)
        
        # Concatenate the selected examples into one string
        examples = "\n".join(examples_list[:shot])

        # Find the language name for better prompting
        source_language_name = self.lang_name_dict.get(source_language) 
        understand_language_name = self.lang_name_dict.get(understander_language)
        
        # Format the prompt using your understand_prompt template
        prompt = mathML_understand_prompt.format(source_language=source_language_name,
                                        examples=examples,
                                        native_question=native_question,
                                        understander_language=understand_language_name)
        return prompt



    # Solver prompt format
    def solver_prompt(self,
                      native_question: str,
                      understanding: str,
                      understander_language: str,
                      source_language: str) -> str:
        
        final_format = self.final_format_dict.get(source_language, self.final_format_dict["en"])  # fallback to English
        
        # Find the language name for better prompting
        source_language_name = self.lang_name_dict.get(source_language) 
        understand_language_name = self.lang_name_dict.get(understander_language)
        
        prompt = solver_prompt.format(native_question=native_question,
                                      understanding=understanding,
                                      understand_language=understand_language_name,
                                      final_format=final_format)
        
        return prompt


    # Solver prompt format
    def clp_solver_prompt(self,
                      native_question: str,
                      understanding: str,
                      understander_language: str,
                      source_language: str) -> str:
        
        final_format = self.final_format_dict.get(source_language, self.final_format_dict["en"])  # fallback to English
        
        # Find the language name for better prompting
        source_language_name = self.lang_name_dict.get(source_language) 
        understand_language_name = self.lang_name_dict.get(understander_language)
        
        prompt = clp_solver_prompt.format(native_question=native_question,
                                      understanding=understanding,
                                      understand_language=understand_language_name,
                                      final_format=final_format)
        
        return prompt

    # Solver prompt format
    def mathML_solver_prompt(self,
                      native_question: str,
                      understanding: str,
                      understander_language: str,
                      source_language: str) -> str:
        
        final_format = self.final_format_dict.get(source_language, self.final_format_dict["en"])  # fallback to English
        
        # Find the language name for better prompting
        source_language_name = self.lang_name_dict.get(source_language) 
        understand_language_name = self.lang_name_dict.get(understander_language)
        
        prompt = mathML_solver_prompt.format(native_question=native_question,
                                      understanding=understanding,
                                      understand_language=understand_language_name,
                                      final_format=final_format)
        
        return prompt


    # Understander prompt format
    def math_ml_prompt(self,
                       source_language: str,
                       understander_language: str,
                       shot: int,
                       native_question: str) -> str:
        
        # Build the variable name
        list_name = f"ml_example_list"
        
        # Check if that variable exists in globals
        if list_name not in globals():
            raise ValueError(f"No examples found for language: {source_language}")
        
        # Retrieve the list of examples
        examples_list = globals()[list_name]
        
        # Ensure the requested shot does not exceed available examples
        if shot > len(examples_list):
            shot = len(examples_list)
        
        # Concatenate the selected examples into one string
        examples = "\n".join(examples_list[:shot])

        # Find the language name for better prompting
        understand_language_name = self.lang_name_dict.get(understander_language)

        final_format = self.final_format_dict.get(understander_language, self.final_format_dict["en"])  # fallback to English
        
        # Format the prompt using your understand_prompt template
        prompt = mathML_prompt.format(examples=examples,
                                      native_question=native_question,
                                      understander_language=understand_language_name,
                                      final_format=final_format)
        return prompt
    








    #################################
    # Answer extraction
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




































