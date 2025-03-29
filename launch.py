# launch.py
import os
import subprocess

languages = ['es', 'fr']
gpus = ['0', '1']

for lang, gpu in zip(languages, gpus):
    cmd = [
        "python", "evaluate_mmlu.py",
        "--lang", lang
    ]
    env = dict(os.environ, CUDA_VISIBLE_DEVICES=gpu)
    subprocess.Popen(cmd, env=env)

print("Both experiments launched in parallel.")
