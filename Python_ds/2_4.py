# 2_4 How to standardize numeric fields using python
import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {'Feature1': [100, 20, 40, 120, 44],
        'Feature2': [5, 4, 5, 4, 5]}

df = pd.DataFrame(data)
print("Original dataset:")
print(df)
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print("\nStandardized dataset:")
print(df_scaled)
