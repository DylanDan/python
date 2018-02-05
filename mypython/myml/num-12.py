#! /usr/bin/python
#-*-coding:utf-8 -*-

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

path = ".\\vhm1eU.csv"
names = ['preg','plas','pres','skin','test','mass', 'pedi', 'age', 'class']
dataf = read_csv(path,names=names)
data = dataf.values
X = data[:,0:8]
Y = data[:,8]

num_trees = 100
max_features = 4

kfold = KFold(n_splits=10,random_state=7)
model = RandomForestClassifier(n_estimators=num_trees,max_features=max_features)
results = cross_val_score(model,X,Y,cv=kfold)
print(results.mean())
