# 3_3 How to construct histograms with overlay using python
import matplotlib.pyplot as plt
import numpy as np

data_1 = np.random.normal(0, 1, 500)
data_2 = np.random.normal(3, 1.5, 50)

plt.hist(data_1, bins=20, color='teal', alpha=0.6, label='Data 1')
plt.hist(data_2, bins=20, color='coral', alpha=0.6, label='Data 2')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Overlay')

plt.legend()
plt.show()
