#! /usr/bin/python
#-*-coding:utf-8 -*-

from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

# path = '..\\..\\mydata\\iris.data'  # 数据文件路径
# data = pd.read_csv(path, header=None)
# x = data[list(range(4))]
# le = LabelEncoder()
# print(data[4])
# result_1 = le.fit_transform(data[4])
# # print(result_1)
# iris_class = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica','Iris-setosa']
# le = LabelEncoder()
# le.fit([1,5,67,100])
# # result = le.transform([1,1,100,67,5,1])
# # [1-0,5-1,8-2,67-3,100-4]
# # data = np.array([[1,3,4],[5,6,7]])
# # print(data)
# result_1 = le.fit_transform(iris_class)
# # print(result)
# print(result_1)

# x = np.linspace(-3,3,50)
# print(x)
# y = x.reshape(1,-1)
# print(y)

depth = [2, 4, 6, 8, 10]
clr = 'rgbmy'
for d, c in zip(depth, clr):
    print (d,c)