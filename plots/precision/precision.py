import numpy as np
import matplotlib.pyplot as plt

# Languages (just for reference; we don't annotate them on the plot)
languages = ['Amh','Ewe','Hau','Ibo','Kin','Lin','Lug','Orm','Sna','Sot','Swa','Twi','Vai','Wol','Xho','Yor','Zul']

# Precision and Accuracy data per method
precision = {
    'COT':  np.array([0.83, 0.07, 0.05, 0.55, 0.63, 0.26, 0.38, 0.32, 0.63, 0.55, 0.89, 0.04, 0.04, 0.07, 0.61, 0.42, 0.66]),
    'CLML': np.array([0.79, 0.08, 0.04, 0.57, 0.65, 0.25, 0.37, 0.30, 0.61, 0.57, 0.85, 0.04, 0.05, 0.07, 0.58, 0.39, 0.63]),
    'CPAL': np.array([0.78, 0.08, 0.04, 0.55, 0.67, 0.29, 0.38, 0.42, 0.65, 0.59, 0.87, 0.06, 0.07, 0.10, 0.59, 0.45, 0.64]),
    'CLP':  np.array([0.84, 0.10, 0.05, 0.64, 0.69, 0.34, 0.44, 0.44, 0.72, 0.59, 0.88, 0.09, 0.10, 0.11, 0.65, 0.52, 0.69])
}

accuracy = {
    'COT':  np.array([69.10, 5.30, 59.00, 38.63, 54.43, 16.43, 29.93, 24.53, 48.47, 42.53, 81.93,  7.67,  3.08,  5.60, 41.27, 30.40, 50.90]),
    'CLML': np.array([67.27, 4.90, 61.00, 44.03, 58.70, 15.17, 32.00, 24.97, 47.27, 46.97, 83.57,  6.83,  3.17,  4.90, 41.87, 32.77, 50.17]),
    'CPAL': np.array([66.27, 5.93, 60.63, 42.87, 56.67, 18.17, 29.83, 30.67, 54.93, 45.53, 80.50,  7.93,  3.31,  5.97, 41.93, 32.40, 48.17]),
    'CLP':  np.array([70.83, 5.53, 65.50, 46.97, 60.43, 19.00, 35.23, 36.40, 57.73, 49.73, 85.63,  9.13,  3.18,  7.40, 46.87, 39.87, 54.57])
}

# Plot
plt.figure(figsize=(8,6))
markers = {'COT':'o', 'CLML':'s', 'CPAL':'^', 'CLP':'D'}
colors  = {'COT':'#1f77b4', 'CLML':'#ff7f0e', 'CPAL':'#2ca02c', 'CLP':'#d62728'}

for method in precision:
    plt.scatter(
        precision[method],
        accuracy[method],
        label=method,
        marker=markers[method],
        color=colors[method],
        edgecolor='black',
        s=80,
        alpha=0.8
    )

plt.xlabel('Precision Score', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
# no plt.title()

plt.legend(title='Method', loc='upper left')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.savefig('precision_vs_accuracy_scatter.png', dpi=300)
plt.show()
