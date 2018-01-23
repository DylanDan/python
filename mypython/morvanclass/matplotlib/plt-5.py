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
plt.plot(x,y_2)
plt.plot(x,y_1,c='red',linewidth=1.0,linestyle='--')

plt.xlim(-1,1)
plt.ylim(-2,2)

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', -1))
ax.spines['left'].set_position(('data',0))
plt.show()
