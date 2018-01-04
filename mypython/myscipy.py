#! /usr/bin/python
#-*-coding:utf-8 -*-

import numpy as np
import scipy.stats as sta

data = np.random.random_sample(900)

# print data

Mean,std = sta.norm.fit(data)

print Mean , std

print sta.skewtest(data)
print sta.kurtosistest(data)
print sta.normaltest(data)
print sta.scoreatpercentile(data,50)
print sta.scoreatpercentile(data,1)

import matplotlib.pyplot as plt

plt.hist(data)
plt.show()
