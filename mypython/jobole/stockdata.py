#! /usr/bin/python
#-*-coding:utf-8 -*-
# http://python.jobbole.com/87813/
# http://python.jobbole.com/88256/

import matplotlib.pylab as plt
import pandas as pd

apple = pd.read_csv("..\\mydata\\APPL.csv")

print(apple.head(5))
# plt.rcParams['figure.figsize']=(15,9)

# apple["Adj Close"].plot(grid=True)

# plt.show()

price = apple['Adj Close']
date = apple['Date']

data = apple.loc[:,['Date','Adj Close']]

# print(data)
# data.plot(x='Date',y='Adj Close',grid=True)
# plt.grid(axis=[price,date])
# plt.griddata(date,price)
data.plot(x='Date',y='Adj Close')
plt.grid(True)

plt.show()
