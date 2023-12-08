# Logistic Regression modelling
# 11_1 How to perform logistic regression modelling.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = {'feature1': [2, 3, 4, 5, 3, 2, 4, 5, 6, 7],
        'feature2': [1, 2, 3, 4, 2, 1, 3, 4, 5, 6],
        'target_variable': [0, 1, 0, 1, 1, 0, 1, 0, 1, 0]}

df = pd.DataFrame(data)

X = df[['feature1', 'feature2']]
y = df['target_variable']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logreg_model = LogisticRegression()
logreg_model.fit(X_train, y_train)

y_pred = logreg_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')
