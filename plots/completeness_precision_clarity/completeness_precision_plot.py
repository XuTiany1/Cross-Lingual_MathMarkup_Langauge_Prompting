import numpy as np
import matplotlib.pyplot as plt

# Data
categories = ['Completeness', 'Precision', 'Clarity']
methods = ['COT', 'CLML', 'CPAL', 'CLP']
scores = {
    'COT':  [0.51, 0.41, 0.49],
    'CLML': [0.47, 0.40, 0.50],
    'CPAL': [0.53, 0.42, 0.50],
    'CLP':  [0.56, 0.46, 0.48]
}

# Colors (soft pastel)
colors = ['#aec7e8', '#ff9896', '#ffbb78', '#98df8a']  # light blue, light red, light yellow, light green

# Plot
x = np.arange(len(categories))  # label locations
bar_width = 0.18

fig, ax = plt.subplots(figsize=(8,4))

for idx, method in enumerate(methods):
    offset = (idx - 1.5) * bar_width
    ax.bar(x + offset, scores[method], width=bar_width, label=method, color=colors[idx], edgecolor='black', alpha=0.8)

# Axis settings
ax.set_ylabel('Score', fontsize=12)
ax.set_ylim(0, 0.7)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.legend(loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.15), frameon=False)

# Add value labels
for idx, method in enumerate(methods):
    offset = (idx - 1.5) * bar_width
    for i, val in enumerate(scores[method]):
        ax.text(x[i] + offset, val + 0.01, f'{val:.2f}', ha='center', va='bottom', fontsize=8)

# Layout
plt.tight_layout()
fig.savefig('understanding_quality.pdf', bbox_inches='tight')

