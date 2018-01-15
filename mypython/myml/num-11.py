#! /usr/bin/python
#-*-coding:utf-8 -*-

from pandas import read_csv
import numpy
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

path = ".\\vhm1eU.csv"
names = ['preg','plas','pres','skin','test','mass', 'pedi', 'age', 'class']
dataf = read_csv(path,names=names)
data = dataf.values
X = data[:,0:8]
Y = data[:,8]

alphas = numpy.array([1,0.1,0.01,0.001,0.0001,0])
param_grid = dict(alpha=alphas)
model = Ridge()
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid.fit(X, Y)
print(grid.best_score_)
print(grid.best_estimator_.alpha)