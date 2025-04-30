

# ==============================
# Deepseek prompts
# ==============================
ds_native_language_prompt = '''
Your answer MUST end with the format: "Answer is A, B, C, or D"
As an expert, choose the most accurate answer to the question below. 
Your goal is to select the correct option ’A’, ’B’, ’C’, or ’D’ by understanding the nuances of the topic.
Your answer MUST end with the format: "Answer is A, B, C, or D"

Question: {question} 
A: {choice1} 
B: {choice2} 
C: {choice3} 
D: {choice4} 
Answer:
'''


ds_english__prompt = '''
Think and reason the question using English language.
Your answer MUST end with the format: "Answer is A, B, C, or D"
As an expert, choose the most accurate answer to the question below. 
Your answer MUST end with the format: "Answer is A, B, C, or D"
Think the question using English language.
I emphasize, you need to think in english and answer in english.

Question: {question} 
A: {choice1} 
B: {choice2} 
C: {choice3} 
D: {choice4} 
Answer:
'''





# ==============================
# COT prompts
# ==============================
qw_native_language_prompt = '''

You are a reasoning model and reason your answer step by step, think step by step. 
Your answer MUST end with the format: "Answer is A, B, C, or D"
As an expert, choose the most accurate answer to the question below. 
Your goal is to select the correct option ’A’, ’B’, ’C’, or ’D’ by understanding the nuances of the topic.
Your answer MUST end with the format: "Answer is A, B, C, or D"

Question: {question} 
A: {choice1} 
B: {choice2} 
C: {choice3} 
D: {choice4} 
Answer:
'''


qw_english__prompt = '''

Answer the question using English language.
You are a reasoning model and reason your answer step by step, think step by step. 
Your answer MUST end with the format: "Answer is A, B, C, or D"
As an expert in, choose the most accurate answer to the question below. 
Your goal is to select the correct option ’A’, ’B’, ’C’, or ’D’ by understanding the nuances of the topic.
You are a reasoning model and reason your answer step by step. 
Your answer MUST end with the format: "Answer is A, B, C, or D"
Answer the question using English language.
I emphasize, you need to think in english and answer in english.

Question: {question} 
A: {choice1} 
B: {choice2} 
C: {choice3} 
D: {choice4} 
Answer:
'''




#========================================== Chinese Option ========================================== 

# ==============================
# Deepseek 提示语
# ==============================
dsc_native_language_prompt = '''
你的答案必须以以下格式结束："Answer is A, B, C, or D"
作为一名专家，请选择下面问题中最准确的答案。
你的目标是通过理解该主题的细微差别，选择正确的选项 'A'、'B'、'C' 或 'D'。
你的答案必须以以下格式结束："Answer is A, B, C, or D"

问题：{question} 
A：{choice1} 
B：{choice2} 
C：{choice3} 
D：{choice4} 
答案：
'''


dsc_english__prompt = '''
请使用英语回答问题。
你的答案必须以以下格式结束："Answer is A, B, C, or D"
作为一名专家，请选择下面问题中最准确的答案。
你的目标是通过理解该主题的细微差别，选择正确的选项 'A'、'B'、'C' 或 'D'。
你的答案必须以以下格式结束："Answer is A, B, C, or D"
请使用英语回答问题。
我强调，你需要用英语思考并用英语回答。

问题：{question} 
A：{choice1} 
B：{choice2} 
C：{choice3} 
D：{choice4} 
答案：
'''


# ==============================
# COT 提示语
# ==============================
qwc_native_language_prompt = '''

你是一个推理模型，请逐步推理你的答案，一步一步思考。
你的答案必须以以下格式结束："Answer is A, B, C, or D"
作为一名专家，请选择下面问题中最准确的答案。
你的目标是通过理解该主题的细微差别，选择正确的选项 'A'、'B'、'C' 或 'D'。
你的答案必须以以下格式结束："Answer is A, B, C, or D"

问题：{question} 
A：{choice1} 
B：{choice2} 
C：{choice3} 
D：{choice4} 
答案：
'''


qwc_english__prompt = '''

请使用英语回答问题。
你是一个推理模型，请逐步推理你的答案，一步一步思考。
你的答案必须以以下格式结束："Answer is A, B, C, or D"
作为一名专家，请选择下面问题中最准确的答案。
你的目标是通过理解该主题的细微差别，选择正确的选项 'A'、'B'、'C' 或 'D'。
你是一个推理模型，请逐步推理你的答案。
你的答案必须以以下格式结束："Answer is A, B, C, or D"
请使用英语回答问题。
我强调，你需要用英语思考并用英语回答。

问题：{question} 
A：{choice1} 
B：{choice2} 
C：{choice3} 
D：{choice4} 
答案：
'''






