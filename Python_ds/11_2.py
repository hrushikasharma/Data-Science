# 11_2 How to perform Poisson regression using python
import pandas as pd
import statsmodels.api as sm

data_new = {'response': [1, 0, 2, 3, 1, 4, 3, 2, 1, 0],
            'predictor1': [2, 4, 1, 3, 5, 2, 6, 1, 7, 2],
            'predictor2': [0, 1, 1, 0, 1, 0, 1, 1, 0, 1]}

df_new = pd.DataFrame(data_new)

X_new = df_new[['predictor1', 'predictor2']]
y_new = df_new['response']

X_new = sm.add_constant(X_new)

poisson_model_new = sm.Poisson(y_new, X_new)
poisson_results_new = poisson_model_new.fit()

print(poisson_results_new.summary())
