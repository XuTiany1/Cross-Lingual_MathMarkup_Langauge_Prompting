import json


def load_reasoning_dict(file1, file2):
   # Load both files into dictionaries keyed by question
   with open(file1, 'r', encoding='utf-8') as f1:
       data1 = {json.loads(line)['question']: json.loads(line)['model_reasoning'] for line in f1}
  
   with open(file2, 'r', encoding='utf-8') as f2:
       data2 = {json.loads(line)['question']: json.loads(line)['model_reasoning'] for line in f2}


   # Combine them into a final dictionary
   combined = {}
   for question in data1:
       if question in data2:
           combined[question] = [data1[question], data2[question]]
       else:
           print(f"Warning: question not found in second language file: {question}")


   return combined




def load_reasoning_dict_all_lang(list_of_file_paths):
    # Load each file into a dictionary (keyed by question) and store in a list.
    data_list = []
    for file_path in list_of_file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = {json.loads(line)['question']: json.loads(line)['model_reasoning'] for line in f}
            data_list.append(data)
    
    # Start with the keys from the first file.
    common_questions = set(data_list[0].keys())
    # For each subsequent file, warn for any missing questions and update the common keys.
    for idx, data in enumerate(data_list[1:], start=2):
        missing = common_questions - set(data.keys())
        for question in missing:
            print(f"Warning: question not found in file {list_of_file_paths[idx-1]}: {question}")
        common_questions &= set(data.keys())
    
    # Build the combined dictionary with lists of model_reasoning from each file.
    combined = {}
    for question in common_questions:
        combined[question] = [data[question] for data in data_list]
    
    return combined
