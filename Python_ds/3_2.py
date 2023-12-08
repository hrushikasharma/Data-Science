# 3_2 How to construct contingency tables using python
import pandas as pd

# Sample data
data = {'Category1': ['A', 'A', 'B', 'B', 'A', 'B'],
        'Category2': ['X', 'Y', 'X', 'Y', 'X', 'Y']}
df = pd.DataFrame(data)

# Create a contingency table
contingency_table = pd.crosstab(df['Category1'], df['Category2'])

# Display the contingency table
print("Contingency Table:")
print(contingency_table)
