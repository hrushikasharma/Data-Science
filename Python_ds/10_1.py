# 10_1 Demonstrate how you will identify multicollinearity in python.
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

data = {'feature1': [2, 4, 1, 3, 5, 2, 6, 1, 7, 2],
        'feature2': [1, 3, 2, 4, 2, 1, 3, 4, 5, 6],
        'feature3': [3, 2, 5, 1, 4, 6, 2, 4, 1, 3]}

df = pd.DataFrame(data)
X = df[['feature1', 'feature2', 'feature3']]
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_data)
