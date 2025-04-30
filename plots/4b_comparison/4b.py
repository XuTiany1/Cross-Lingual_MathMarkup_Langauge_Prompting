import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 1. Define language families and methods
families = [
    "Niger-Congo / Bantu", "Niger-Congo / Kwa", "Afro-Asiatic / Chadic",
    "Afro-Asiatic / Ethio-Semitic", "Niger-Congo / Volta-Niger",
    "Afro-Asiatic / Cushitic", "Niger-Congo / Senegambia", "Mande"
]
methods = ["SEnglish COT", "SEnglish CLML", "SEnglish CPAL", "SEnglish CLP"]

# 2. Input the 4B and 12B accuracies for each
data_4b = {
    "SEnglish COT":  [19.77, 3.20, 28.80, 49.60, 9.00, 5.20, 2.80, 0.40],
    "SEnglish CLML": [18.69, 4.20, 23.60, 46.40, 7.60, 5.20, 3.20, 1.70],
    "SEnglish CPAL":[24.00, 5.00, 31.60, 50.80, 7.00, 7.60, 2.80, 2.40],
    "SEnglish CLP": [25.66, 4.60, 35.20, 51.20, 10.60, 5.26, 2.80, 2.40],
}
data_12b = {
    "SEnglish COT":  [45.89, 7.20, 60.80, 70.00, 35.60, 26.00, 5.60, 3.20],
    "SEnglish CLML": [48.00, 6.00, 62.00, 68.80, 41.00, 26.40, 4.40, 3.40],
    "SEnglish CPAL":[49.54, 6.80, 62.80, 69.20, 41.60, 36.40, 6.00, 3.10],
    "SEnglish CLP": [53.03, 8.40, 67.20, 73.20, 46.00, 38.40, 7.20, 3.40],
}

# 3. Create DataFrames and compute improvements
df4b = pd.DataFrame(data_4b, index=families)
df12b = pd.DataFrame(data_12b, index=families)
df_imp = df12b - df4b

# 4. Plotting
plt.rcParams.update({"font.size": 10})
fig, ax = plt.subplots(figsize=(14, 7))
x = np.arange(len(families))
bar_width = 0.18

# Define your custom colors from your image
colors = [
    "#aec7e8",  # COT - light blue
    "#f7b6d2",  # CLML - pink
    "#ffbb78",  # CPAL - orange
    "#98df8a",  # CLP - light green
]

# Draw the bars
for i, m in enumerate(methods):
    xs = x + (i - (len(methods)-1)/2) * bar_width
    ax.bar(xs, df4b[m], bar_width, color=colors[i], label=m)
    ax.bar(xs, df_imp[m], bar_width,
           bottom=df4b[m],
           color=colors[i],
           hatch='//',
           label="_nolegend_")

# 5. Legend
method_patches = [mpatches.Patch(facecolor=colors[i], label=methods[i]) for i in range(len(methods))]
imp_patch = mpatches.Patch(facecolor='white', edgecolor='black', hatch='//', label='12B improvement')
ax.legend(handles=method_patches + [imp_patch], bbox_to_anchor=(1.02, 1), loc="upper left")

# 6. Labels and formatting
ax.set_xticks(x)
ax.set_xticklabels(families, rotation=30, ha='right')
for label in ax.get_xticklabels():
    label.set_fontsize(12)
    label.set_fontweight('bold')
ax.set_ylabel("Accuracy (%)")
ax.set_xlabel("Language Family")
ax.set_title("Accuracy Comparison of 4B and 12B Across Language Families")
plt.tight_layout(pad=2)
plt.subplots_adjust(right=0.75, bottom=0.25)

# 7. Save
plt.savefig("accuracy_comparison_4B_12B.png", dpi=300)
plt.show()
