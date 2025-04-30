import numpy as np
import matplotlib.pyplot as plt

# 1) Define languages and scores
languages = [
    'Amh','Ewe','Hau','Ibo','Kin','Lin','Lug','Orm','Sna','Sot','Swa','Twi','Vai','Wol','Xho','Yor','Zul'
]
completeness = {
    'COT':  np.array([0.89, 0.14, 0.05, 0.70, 0.74, 0.39, 0.50, 0.45, 0.74, 0.68, 0.92, 0.09, 0.09, 0.15, 0.73, 0.56, 0.76]),
    'CLML': np.array([0.85, 0.13, 0.04, 0.65, 0.72, 0.34, 0.45, 0.38, 0.69, 0.65, 0.89, 0.07, 0.06, 0.11, 0.67, 0.49, 0.72]),
    'CPAL': np.array([0.86, 0.15, 0.05, 0.70, 0.79, 0.46, 0.51, 0.59, 0.77, 0.72, 0.92, 0.10, 0.07, 0.21, 0.72, 0.59, 0.77]),
    'CLP':  np.array([0.89, 0.17, 0.06, 0.76, 0.79, 0.49, 0.57, 0.59, 0.81, 0.72, 0.91, 0.16, 0.14, 0.20, 0.75, 0.68, 0.78])
}
accuracy = {
    'COT':  np.array([69.10, 5.30, 59.00, 38.63, 54.43, 16.43, 29.93, 24.53, 48.47, 42.53, 81.93, 7.67, 3.08, 5.60, 41.27, 30.40, 50.90]),
    'CLML': np.array([67.27, 4.90, 61.00, 44.03, 58.70, 15.17, 32.00, 24.97, 47.27, 46.97, 83.57, 6.83, 3.17, 4.90, 41.87, 32.77, 50.17]),
    'CPAL': np.array([66.27, 5.93, 60.63, 42.87, 56.67, 18.17, 29.83, 30.67, 54.93, 45.53, 80.50, 7.93, 3.31, 5.97, 41.93, 32.40, 48.17]),
    'CLP':  np.array([70.83, 5.53, 65.50, 46.97, 60.43, 19.00, 35.23, 36.40, 57.73, 49.73, 85.63, 9.13, 3.18, 7.40, 46.87, 39.87, 54.57])
}

# 2) Plot configuration
markers = {'COT':'o', 'CLML':'s', 'CPAL':'^', 'CLP':'D'}
colors  = {'COT':'#1f77b4', 'CLML':'#ff7f0e', 'CPAL':'#2ca02c', 'CLP':'#d62728'}

plt.figure(figsize=(8,6))
for method in ['COT','CLML','CPAL','CLP']:
    plt.scatter(
        completeness[method],
        accuracy[method],
        label=method,
        marker=markers[method],
        color=colors[method],
        edgecolor='black',
        s=80,
        alpha=0.8
    )

# 3) Labels, legend, grid
plt.xlabel('Completeness Score', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
plt.legend(title='Method', loc='upper left')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# 4) Save or show
plt.tight_layout()
plt.savefig('completeness_accuracy_scatter.png', dpi=300)
plt.show()
