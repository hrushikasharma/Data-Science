# 10_2 Demonstrate how you will apply principal components analysis using python
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

new_data = {'feature_x': [4, 6, 2, 5, 3, 2, 7, 1, 8, 3],
            'feature_y': [2, 4, 1, 3, 5, 2, 6, 1, 7, 2],
            'feature_z': [1, 3, 2, 4, 2, 1, 3, 4, 5, 6]}

df_new = pd.DataFrame(new_data)

scaler_new = StandardScaler()
df_scaled_new = scaler_new.fit_transform(df_new)

pca_new = PCA(n_components=2)
pca_result_new = pca_new.fit_transform(df_scaled_new)

df_pca_new = pd.DataFrame(data=pca_result_new, columns=['PC1', 'PC2'])

plt.scatter(df_pca_new['PC1'], df_pca_new['PC2'])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Result')
plt.show()
