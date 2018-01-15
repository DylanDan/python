#! /usr/bin/python
#-*-coding:utf-8 -*-
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

path = ".\\vhm1eU.csv"
names = ['preg','plas','pres','skin','test','mass', 'pedi', 'age', 'class']
dataf = read_csv(path,names=names)
data = dataf.values
X = data[:,0:8]
Y = data[:,8]
models = []
models.append(('LR',LogisticRegression()))
models.append(('LDA',LinearDiscriminantAnalysis()))

results = []
names = []
scoring = 'accuracy'
for name,model in models:
    kfold = KFold(n_splits=10,random_state=7)
    cv_result = cross_val_score(model,X,Y,scoring=scoring)
    results.append(cv_result)
    results.append(name)
    msg = "%s:%f (%f)" % (name,cv_result.mean(),cv_result.std())
    print(msg)
