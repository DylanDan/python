import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("..\\mydata\\ccpp.csv")

X = data[['AT', 'V', 'AP', 'RH']]
Y = data[['PE']]
x_train,x_test,y_train,y_test = train_test_split(X,Y,random_state=1)
model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mse  = metrics.mean_squared_error(y_test,y_pred)
rmse = np.sqrt(metrics.mean_squared_error(y_test,y_pred))

print(y_test.dtpyes)
print(type(y_pred))

print(y_test.values.shape)
print(y_pred.shape)

a = np.arange(10)
b = np.arange(10)

print(type(a))
print(type(b))

accuracy = metrics.accuracy_score(y_test.values,y_pred)

print("MES is : %f" % mse)
print("RMES is : %f" % rmse)
print("accuracy is : %f" % accuracy)


