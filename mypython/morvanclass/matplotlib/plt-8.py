#! /usr/bin/python
#-*-coding:utf-8 -*-

import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 0.1*x

plt.figure(num=1,figsize=(8,5))
plt.plot(x,y,lw='10')

plt.ylim(-2,2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor='b',alpha=0.7,zorder=2))


plt.show()
