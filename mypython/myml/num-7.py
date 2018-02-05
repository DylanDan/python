#! /usr/bin/python
#-*-coding:utf-8 -*-

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

path = ".\\vhm1eU.csv"
names = ['preg','plas','pres','skin','test','mass', 'pedi', 'age', 'class']
dataf = read_csv(path,names=names)
data = dataf.values
X = data[:,0:8]
Y = data[:,8]
kflod = KFold(n_splits=10,random_state=7)
model = LogisticRegression()
result = cross_val_score(model,X,Y,cv=kflod)
print("Accuracy: ")
print(result.mean()*100.0)
print("Accuracy: ")
print(result.std()*100.0)
print(result)


