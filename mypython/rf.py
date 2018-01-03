
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.datasets import load_iris

iris=load_iris();
print(iris)
print(iris['target'].shape)
print(iris['data'].shape)

rf=RandomForestRegressor()
rf.fit(iris.data[:150],iris.target[:150])

instance=iris.data[[100,109]]
# print(instance)
print(instance[0])

print('instance 0 prediction:',rf.predict(instance[0].reshape(1,-1)))
print(iris.target[100])


