# -*- coding: utf-8 -*-
"""Spark_Foundation_Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QH2qP8EYSewTrJVm61A1GhaxUFHDwAo3

**Importing Libraries & Reading Data [Darshil Shah]**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://bit.ly/w-data")
print("Imported Data is")
df.head(10)

"""**Visualizing Data to find Patterns**"""

df.plot(x="Hours", y="Scores", style="o")
plt.title("Hours vs Percentage")
plt.xlabel("Hours studied")
plt.ylabel("Percentage scored")

"""**Preparing Data**"""

X = df.iloc[:,:-1].values
y = df.iloc[:,1].values

"""**Training Data**"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=0)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

"""**Visualizing Regression Line**"""

line = regression.coef_*X+regression.intercept_

plt.scatter(X,y)
plt.plot(X, line)

"""**Predicting**"""

y_pred = regression.predict(X_test)
print("Predicted Values of X, Y")
for i in range(len(X_test)):
  print(X_test[i],y_pred[i])

"""**Evaluating Model**"""

from sklearn import metrics
print("Mean Absolute Error:",metrics.mean_absolute_error(y_test,y_pred))