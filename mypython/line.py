#! /usr/bin/python
#-*- coding:utf-8 -*-
'''
Created on 2018-1-3

@author: Dylan.Dan
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from bokeh.charts.attributes import color

xmin,xmax = -5,5
n_samples = 100
np.random.seed(0)
X=np.random.normal(size=n_samples)
# print X
y = (X>0).astype(np.float)
# print y
X[X>0] *=4
# print X
X+=.3*np.random.normal(size=n_samples)
# print X
X = X[:,np.newaxis]
clf = linear_model.LogisticRegression(C=1e5)
clf.fit(X,y)

plt.figure(1, figsize=(4,3))
plt.clf()
plt.scatter(X.ravel(),y,color='black',zorder=20)
X_test = np.linspace(-5,10,300)
print X_test


def model(x):
    return 1/(1+np.exp(-x))

loss = model(X_test*clf.coef_+clf.intercept_).ravel()
plt.plot(X_test,loss,color='red',linewidth=3)

ols = linear_model.LinearRegression()
ols.fit(X, y)
plt.plot(X_test,ols.coef_*X_test+ols.intercept_,linewidth=1)
plt.axhline(.5,color='.5')

plt.ylabel('y')
plt.xlabel('x')
plt.xticks(range(-5,10))
plt.yticks([0,0.5,1])
plt.ylim(-.25,1.25)
plt.xlim(-4,10)
plt.legend(('logistic Regression Model','Linear Regression Model'),loc='lower right',fontsize='small')
plt.show()







