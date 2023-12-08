# 3_4 How to perform binning based on predictive value using python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(123)

data = pd.DataFrame({
    'feature': np.random.randn(1000),
    'target': np.random.choice([0, 1], size=1000, replace=True)
})

data['bins'] = pd.cut(data['feature'], bins=5)

bin_means = data.groupby('bins')['target'].mean().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(x='bins', y='target', data=bin_means, color='blue')
plt.title('Binning Based on Predictive Value')
plt.xlabel('Bins')
plt.ylabel('Mean Target Value')
plt.show()
