# 2_2 How to change misleading fields in python
import pandas as pd

data = {'Fruits': ['Apple', 'Orange', 'Banana', 'Strawberry'],
        'Price': [250, -100, 300, -40],
        'Color': ['Red', 'Orange', 'Yellow', 'Pink']}

df = pd.DataFrame(data)
df_original = df.copy()
df['Price'] = df['Price'].apply(lambda x: x if x > 0 else pd.NA)
print("Original DataFrame:")
print(df_original)
print("\nModified DataFrame:")
print(df)
