# ==============================
# Deepseek MGSM prompts
# ==============================

ds_en_prompt = '''
Answer the question using English language. 
Question: {question}. 
'''

ds_zh_prompt = '''
請用中文回答下列問題：
問題：{question}
'''

ds_bn_prompt = '''
দয়া করে নিচের প্রশ্নের উত্তর বাংলায় দিন:
প্রশ্ন: {question}
'''

ds_de_prompt = '''
Bitte beantworte die folgende Frage auf Deutsch:
Frage: {question}
'''

ds_es_prompt = '''
Por favor, responde la siguiente pregunta en español:
Pregunta: {question}
'''

ds_fr_prompt = '''
Veuillez répondre à la question suivante en français :
Question : {question}
'''

ds_ja_prompt = '''
以下の質問に日本語で答えてください：
質問： {question}
'''

ds_ru_prompt = '''
Пожалуйста, ответьте на следующий вопрос на русском языке:
Вопрос: {question}
'''

ds_sw_prompt = '''
Tafadhali jibu swali lifuatalo kwa Kiswahili:
Swali: {question}
'''

ds_te_prompt = '''
దయచేసి కింది ప్రశ్నకు తెలుగులో సమాధానమివ్వండి:
ప్రశ్న: {question}
'''

ds_th_prompt = '''
กรุณาตอบคำถามต่อไปนี้เป็นภาษาไทย:
คำถาม: {question}
'''

# ==============================
# Deepseek AFRIMGSM prompts
# ==============================


ds_amh_prompt = '''
እባክዎ የሚቀጥለውን ጥያቄ በአማርኛ ብቻ መልስ ይስጡ። እንግሊዝኛ አትጠቀሙ።
ጥያቄ፡ {question}
'''

ds_ewe_prompt = '''
Mègazã Eŋlisigbe o. Ðeko nàɖe biabia sia me le Eŋlisigbe me. 
Nyabiase: {question}
'''

ds_hau_prompt = '''
Don Allah ka ba da amsar tambayar da ke ƙasa a harshen Hausa:
Tambaya: {question}
'''

ds_ibo_prompt = '''
Biko, zaa ajụjụ dị n’okpuru a n’asụsụ Igbo:
Ajụjụ: {question}
'''

ds_kin_prompt = '''
Sobanura igisubizo cy’iki kibazo ukoresheje ururimi rw’Ikinyarwanda:
Ikibazo: {question}
'''

ds_lin_prompt = '''
Yanolá na motuna yango
Svp bo résoudre question étape par étape.
Motuna: {question}.
'''

ds_orm_prompt = '''
Gaaffii kana deebisaa:
Gaaffii: {question}
'''

ds_sna_prompt = '''
Pindura mubvunzo uyu: {question}
'''

ds_sot_prompt = '''
Araba potso e: {question}
'''

ds_twi_prompt = '''
Di asɛmmisa yi ho dwuma: {question}
'''

ds_vai_prompt = '''
{question}
'''

ds_wol_prompt = '''
tontu laaj bii: {question}
'''

ds_xho_prompt = '''
Phendula lo mbuzo: {question}
'''

ds_zulu_prompt = '''
Phendula lo mbuzo: {question}
'''



# ==================
# COT prompts MGSM

cot_en_prompt = '''
Answer the question using English language.
Please solve the question step by step.
Question: {question}.
'''

cot_zh_prompt = '''
請用中文回答下列問題：
請分步驟解答問題。
問題：{question}
'''

cot_bn_prompt = '''
দয়া করে নিচের প্রশ্নের উত্তর বাংলায় দিন:
অনুগ্রহ করে সমস্যাটির সমাধান ধাপে ধাপে ব্যাখ্যা করুন।
প্রশ্ন: {question}
'''

cot_de_prompt = '''
Bitte beantworte die folgende Frage auf Deutsch:
Bitte löse die Frage Schritt für Schritt.
Frage: {question}
'''

cot_es_prompt = '''
Por favor, responde la siguiente pregunta en español:
Por favor, resuelve la pregunta paso a paso.
Pregunta: {question}
'''

cot_fr_prompt = '''
Veuillez répondre à la question suivante en français :
Veuillez résoudre la question étape par étape.
Question : {question}
'''

cot_ja_prompt = '''
以下の質問に日本語で答えてください：
質問を段階的に解いてください。
質問： {question}
'''

cot_ru_prompt = '''
Пожалуйста, ответьте на следующий вопрос на русском языке:
Пожалуйста, решите вопрос пошагово.
Вопрос: {question}
'''

cot_sw_prompt = '''
Tafadhali jibu swali lifuatalo kwa Kiswahili:
Tafadhali, suluhisha swali hili hatua kwa hatua.
Swali: {question}
'''

cot_te_prompt = '''
దయచేసి కింది ప్రశ్నకు తెలుగులో సమాధానమివ్వండి:
దయచేసి ప్రశ్నను దశలవారీగా పరిష్కరించండి.
ప్రశ్న: {question}
'''

cot_th_prompt = '''
กรุณาตอบคำถามต่อไปนี้เป็นภาษาไทย:
กรุณาแก้ปัญหานี้เป็นขั้นตอน ๆ
คำถาม: {question}
'''

# ==================
# COT prompts AFRIMGSM

cot_amh_prompt = '''
እባክዎ የሚቀጥለውን ጥያቄ በአማርኛ ብቻ መልስ ይስጡ። እንግሊዝኛ አትጠቀሙ።
እባክዎ ጥያቄውን በደረጃ በደረጃ ይፍታት።
ጥያቄ፡ {question}
'''

cot_ewe_prompt = '''
Ðo biabia la ŋu.
Taflatse mikpɔ nyabiasea gbɔ afɔɖeɖe ɖesiaɖe.
Nyabiase: {question}.
'''

cot_hau_prompt = '''
Don Allah ka ba da amsar tambayar da ke ƙasa a harshen Hausa:
Don Allah, a warware tambayar a hankali, mataki-mataki.
Tambaya: {question}
'''

cot_ibo_prompt = '''
Biko, zaa ajụjụ dị n’okpuru a n’asụsụ Igbo:
Biko, dozie ajụjụ a site na nzọụkwụ n'ụzọ zuru ezu.
Ajụjụ: {question}
'''

cot_kin_prompt = '''
Sobanura igisubizo cy’iki kibazo ukoresheje ururimi rw’Ikinyarwanda:
Nyamuneka, subiza ikibazo mu ntambwe ku yindi.
Ikibazo: {question}
'''

cot_lin_prompt = '''
Silisa motuna oyo
Tala ntambwe na ntambwe ulambe.
Motuna: {question}
'''

cot_lug_prompt = '''
Ddamu ekibuuzo kino 
Gonjoola mutendera ku mutendera
{question}
'''

cot_orm_prompt = '''
Gaaffii kana deebisaa:
Gaaffii kana kutaa-kutaa furuuf yaalii.
Gaaffii: {question}
'''

cot_sna_prompt = '''
Pindura mubvunzo uyu:
Ndapota, tsanangura mhinduro yako nhanho nhanho.
Mubvunzo: {question}
'''

cot_sot_prompt = '''
Araba potso e:
Ka kopo, araba potso ena ka mehato a mehato.
Potso: {question}
'''

cot_twi_prompt = '''
Bua asɛmmisa yi:
Yɛsrɛ sɛ munni asɛmmisa no ho dwuma anammɔn biara.
Asɛmmisa: {question}
'''

cot_vai_prompt = '''
{question}
[Note: Please provide a step-by-step solution in the Vai language.]
'''

cot_wol_prompt = '''
Tontu laaj bi
Nanga tontu laaj bi jéego ak jéego.
Laaj bi: {question}
'''

cot_xho_prompt = '''
Phendula lo mbuzo:
Nceda uchaze isisombululo sakho ngokwenqanaba, inyathelo nenyathelo.
Mbuzo: {question}
'''

cot_yor_prompt = '''
Yanju ibeere yii ni igbese nipa igbese.
{question}
'''

cot_zul_prompt = '''
Phendula lo mbuzo:
Ngiyacela uchaze izinyathelo zokuxazulula lo mbuzo.
Umbuzo: {question}
'''



# ==============================
# Cross Lingual Prompts
# ==============================

understand_prompt = '''
Given the following problems and the program solutions, please act as an expert in multilingual understanding in {source_language}.
The following are examples of how you should generate the pseudocode given a problem. 
{examples}
Generate pseudocode like the examples you see except that language in comments should be in {understander_language}
Q: {native_question}

'''

solver_prompt = '''
This is the question:
{native_question}
This is your understanding: 
{understanding}
After understanding, you should act as a {understand_language} programmer, 
Provide a single chain-of-thought explanation that includes all intermediate steps in {understand_language}
For clarity at the end you should format your answer as "{final_format}"
'''



clp_understand_prompt = '''
Please act as an expert in multi-lingual understanding in {source_language}.
The following are examples of how you should understand the problem. 
{examples}
After understanding, you should convert it into math markup language.
The following are examples of how you should understand the problem in MathML.
{mathml_examples}

Question: {native_question}
Let’s understand the task in
{understander_language} step-by-step!
Understanding:
'''


clp_solver_prompt = '''
This is the question:
{native_question}
This is your understanding: 
{understanding}
After understanding, you should act as an expert in arithmetic reasoning in
{understand_language}.
Provide a single chain-of-thought explanation that includes all intermediate steps in {understand_language}
For clarity at the end you should format your answer as "{final_format}"
'''


mathML_prompt = '''
For clarity at the end you should format your answer as "{final_format}"
The following are examples of how you should generate MathML given a problem. 
{examples}
Question: {native_question}
First, understand in {understander_language} and convert the question into MathML, then solve it.
'''


mathML_understand_prompt = '''
Please act as an expert in multi-lingual understanding in {source_language}.
The following are examples of how you should understand the problem in MathML.
{examples}
Question: {native_question}
First, understand in {understander_language} and convert the question into MathML
Understanding:
'''


mathML_solver_prompt = '''
This is the question:
{native_question}
This is your mathML understanding: 
{understanding}
After understanding, you should act as an expert in arithmetic reasoning in {understand_language}.
Provide a single chain-of-thought explanation that includes all intermediate steps in {understand_language}
For clarity at the end you should format your answer as "{final_format}"
'''






















