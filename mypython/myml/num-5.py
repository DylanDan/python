#! /usr/bin/python
#-*-coding:utf-8 -*-

import pandas
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix as sm

path = ".\\vhm1eU.csv"
names = ['preg','plas','pres','skin','test','mass', 'pedi', 'age', 'class']
data = pandas.read_csv(path,names=names)
sm(data)
plt.show()

