import numpy as np
import matplotlib.pyplot as plt

# Languages
languages = [
    'Amh','Ewe','Hau','Ibo','Kin','Lin','Lug','Orm','Sna','Sot',
    'Swa','Twi','Vai','Wol','Xho','Yor','Zul','En','Fr'
]

# Difference between CLP and CLML
diff_clp_clml = np.array([
    4.00, 0.13, 6.40, 4.67, 2.93, 4.40, 4.27, 12.00, 12.93, 5.33,
    4.53, 2.13, 0.27, 1.60, 5.20, 8.80, 6.27, 2.67, 2.20
])

# Plot
x = np.arange(len(languages))

fig, ax = plt.subplots(figsize=(12, 5))

# Bar color consistent with earlier pastel look
ax.bar(
    x, diff_clp_clml, 
    color='#98df8a',      # pastel green
    edgecolor='black',    # black edge
    alpha=0.8,            # light transparency
    linewidth=1.0
)

# Axis labels and ticks
ax.set_ylabel('Accuracy Gain (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(languages, rotation=45, ha='right', fontsize=10)
ax.set_ylim(0, max(diff_clp_clml) + 2)

# (No grid lines here anymore)

# Add value labels on top
for i, v in enumerate(diff_clp_clml):
    ax.text(i, v + 0.5, f'{v:.1f}', ha='center', va='bottom', fontsize=8)

# Layout and save
plt.tight_layout()
plt.savefig('difference_clp_clml_no_grid.png', dpi=300)
plt.show()
