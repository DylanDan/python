#! /usr/bin/python
#-*-coding:utf-8 -*-
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

path = ".\\vhm1eU.csv"
names = ['preg','plas','pres','skin','test','mass', 'pedi', 'age', 'class']
dataf = read_csv(path,names=names)
data = dataf.values
X = data[:,0:8]
Y = data[:,8]

test_size = 0.2
seed = 7

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=test_size,random_state=seed)

print("X_train:")
print(X_train)
print("X_test:")
print(X_test)
print("Y_train:")
print(Y_train)
print("Y_test:")
print(Y_test)
print("===================================================================================")

model = LogisticRegression()
model.fit(X_train,Y_train)
filename = 'finalized_model.sav'
pickle.dump(model,open(filename,'wb'))

loaded_model = pickle.load(open(filename,'rb'))
result = loaded_model.score(X_test,Y_test)
print(result)

