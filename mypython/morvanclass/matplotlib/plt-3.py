#! /usr/bin/python
#-*-coding:utf-8 -*-

import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-1,1,50)
y = 2*x + 1
plt.plot(x,y)
plt.show()

