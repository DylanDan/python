#! /usr/bin/python
#-*-coding:utf-8 -*-

import pandas

url = 'https://goo.gl/vhm1eU'
path = ".\\vhm1eU.csv"
names = ['preg','plas','pres','skin','test','mass', 'pedi', 'age', 'class']
data = pandas.read_csv(path,names=names)
print(data.shape)