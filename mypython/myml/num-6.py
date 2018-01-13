#! /usr/bin/python
#-*-coding:utf-8 -*-

from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

path = ".\\vhm1eU.csv"
names = ['preg','plas','pres','skin','test','mass', 'pedi', 'age', 'class']
data = pd.read_csv(path,names=names)

array = data.values

X = array[:,0:8]
print(X)
Y = array[:,8]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
np.set_printoptions(precision=4)
print(rescaledX[0:5,:])
