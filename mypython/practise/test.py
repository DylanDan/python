#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np
# import csv
#
# for y in range(4):
#     print(y)
#
# trainingSet = []
# with open('..\\mydata\\iris.data', 'r') as csvfile:
#     lines = csv.reader(csvfile)
#     dataset = list(lines)
#     print(dataset)
#     for x in range(len(dataset) - 1):
#         for y in range(4):
#             dataset[x][y] = float(dataset[x][y])
#             trainingSet.append(dataset[x])

# distance = []
#
# data1 = [2, 2, 2, 'a']
# x = 0.3332323
#
# distance.append((data1,x))
#
# print(distance)


import pandas as pd
# # import pandas.da datareader as web    # Package and modules for importing data; this code may change depending on pandas version
# import pandas_datareader as web
# import datetime
# start = datetime.datetime(2016,1,1)
# end = datetime.date.today()
#
# apple = web.DataReader("AAPL", "yahoo", start, end)
#
# type(apple)
#
# apple.head()

from pandas_datareader import data as pdr
# data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
data = pdr.get_data_yahoo(["SPY", "IWM"], start="2017-01-01", end="2017-04-30")
print(data.head(5))
import fix_yahoo_finance


