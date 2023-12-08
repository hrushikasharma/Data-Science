# 4_2 How to balance the training data set
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
from sklearn.datasets import load_iris
from collections import Counter

data = load_iris()
X, y = data.data, data.target

print("Class distribution before balancing:", Counter(y))

under_sampler = RandomUnderSampler(sampling_strategy='auto', random_state=42)
X_resampled, y_resampled = under_sampler.fit_resample(X, y)

print("Class distribution after balancing:", Counter(y_resampled))
