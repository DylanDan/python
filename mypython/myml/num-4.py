#! /usr/bin/python
#-*-coding:utf-8 -*-

import pandas

path = ".\\vhm1eU.csv"
names = ['preg','plas','pres','skin','test','mass', 'pedi', 'age', 'class']
data = pandas.read_csv(path,names=names)
description = data.describe
print("description:")
print(description)
print("=======================================================")
print("head:")
print(data.head())
print("=======================================================")
print("dtypes:")
print(data.dtypes)
print("=======================================================")
print("corr:")
#TODO need to understand corr
print(data.corr())
print("=======================================================")
