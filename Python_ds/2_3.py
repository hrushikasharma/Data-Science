# 2_3 How to re express categorical field values using python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {'LaptopBrand': ['Dell', 'HP', 'Lenovo', 'HP', 'Dell', 'Lenovo']}
df = pd.DataFrame(data)
label_encoder = LabelEncoder()
df['LaptopBrand'] = label_encoder.fit_transform(df['LaptopBrand'])
print(df)
