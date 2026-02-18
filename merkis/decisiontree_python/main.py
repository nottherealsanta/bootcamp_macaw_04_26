from DecisionTree import DecisionTree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
import numpy as np

data = datasets.load_breast_cancer()

X, y = data.data, data.target
X = pd.DataFrame(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(np.unique(y_train))




model = DecisionTree()



model.fit(X_train, y_train)

y_test_prediction = model.predict(X_test)

print(f"y_test_prediction: {y_test_prediction}")
print(np.sum(y_test_prediction == y_test)/len(y_test))






