#! /usr/bin/python
#-*-coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)




# Just a figure and one subplot
# f, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')

# Two subplots, unpack the output array immediately
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing Y axis')
# ax2.scatter(x, y)

# # Four polar axes
f, (ax1,ax2) = plt.subplots(2, 2, subplot_kw=dict(polar=True))
ax1[0].plot(x, y)
ax1[1].plot(x, y)
ax2[0].plot(x, y)
ax2[0].plot(x, y)

#
# # Share a X axis with each column of subplots
plt.subplots(2, 2, sharex='col')
#
# # Share a Y axis with each row of subplots
plt.subplots(2, 2, sharey='row')
#
# # Share a X and Y axis with all subplots
plt.subplots(2, 2, sharex='all', sharey='all')

plt.show()
