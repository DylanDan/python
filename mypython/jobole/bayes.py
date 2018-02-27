#! /usr/bin/python
#-*-coding:utf-8 -*-
from IPython.display import Image

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import pymc3 as pm
import scipy
import scipy.stats as stats
#import scipy.optimize as opt
#import statsmodels.api as sm

plt.style.use('bmh')
colors = ['#348ABD', '#A60628', '#7A68A6', '#467821', '#D55E00',
          '#CC79A7', '#56B4E9', '#009E73', '#F0E442', '#0072B2']
messages = pd.read_csv('..\\mydata\\hangout_chat_data.csv')

# fig = plt.figure(figsize=(11,3))
# ax = fig.add_subplot(111)
# x_lim = 60
# mu = [5, 20, 40]
# for i in np.arange(x_lim):
#     plt.bar(i, stats.poisson.pmf(mu[0], i), color=colors[3])
#     plt.bar(i, stats.poisson.pmf(mu[1], i), color=colors[4])
#     plt.bar(i, stats.poisson.pmf(mu[2], i), color=colors[5])
# ax.set_xlim(0, x_lim)
# ax.set_ylim(0, 0.2)
# ax.set_ylabel('Probability mass')
# ax.set_title('Poisson distribution')
# plt.legend(['$mu$ = %s' % mu[0], '$mu$ = %s' % mu[1], '$mu$ = %s' % mu[2]])
# plt.show()
fig = plt.figure(figsize=(11,3))
plt.title('Frequency of messages by response time')
plt.xlabel('Response time (seconds)')
plt.ylabel('Number of messages')
plt.hist(messages['time_delay_seconds'].values,range=[0, 60], bins=60, histtype='stepfilled')
plt.show()