#! /usr/bin/python
#-*-coding:utf-8 -*-

import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-3,3,50)
y_1 = 2*x + 1
y_2 = x**2+1
# plt.figure()
# plt.plot(x,y_1)
plt.figure()


plt.plot(x,y_2,label='up')
plt.plot(x,y_1,c='red',linewidth=1.0,linestyle='--',label='down')
plt.legend(loc='best')


plt.show()
