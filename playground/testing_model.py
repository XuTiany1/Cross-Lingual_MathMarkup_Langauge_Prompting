from vllm import LLM, SamplingParams

llm = LLM(
    model="lightblue/DeepSeek-R1-Distill-Qwen-7B-Multilingual",
    max_model_len=8_000
)

sampling_params = SamplingParams(
    temperature=0.5, 
    max_tokens=8_000
)

prompts = [
    """学校には1クラスにつき20人の生徒がおり、クラスは合計3つあります。
学校全体では男子と女子がそれぞれ50%ずついます。
1つ目のクラスには女子が15人、2つ目のクラスには女子が12人います。
3つ目のクラスには何人の男子がいますか？"""
]

conversations = [
    [{"role": "user", "content": x}] for x in prompts
]

outputs = llm.chat(conversations, sampling_params=sampling_params)

for output in outputs:
    print(output.outputs[0].text)

# <think>
# まず、学校の総生徒数を算出します。各クラスに20人の生徒があり、クラスは3つあるため、総生徒数は60人です。

# 次に、学校全体で男子と女子は同じ人数で分布しています。したがって、男子と女子各有30人。
...
# したがって、3つ目のクラスの男子数は20 - 3 = 17人です。
# </think>

# **解答：**

# 学校の総生徒数を算出します。
...
# **最終的な答え：**
# \[
# \boxed{17}
# \]
