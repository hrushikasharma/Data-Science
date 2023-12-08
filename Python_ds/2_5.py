# 2_5 How to identify outliers in python
import pandas as pd

data = {'Values': [10, 20, 30, 40, 50, 200]}
df = pd.DataFrame(data)
Q1 = df['Values'].quantile(0.25)
Q3 = df['Values'].quantile(0.75)
IQR = Q3 - Q1
outliers = (df['Values'] < (Q1 - 1.5 * IQR)) | (df['Values'] > (Q3 + 1.5 * IQR))

print("Outliers:")
print(df[outliers])
