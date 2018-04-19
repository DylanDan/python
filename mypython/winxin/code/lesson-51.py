# !/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-notebook')
import seaborn as sns
sns.set()
import matplotlib.cm as cm
import pandas_datareader as pdr
# Enable logging
import logging
import sys
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')


column_names = ['Ticker', 'Security', 'GICS_Sector', 'GICS_Sub_Industry', 'Address', 'Date_added', 'CIK']
sp500companies = pd.read_csv('../data/500company.csv', header=0, names=column_names).drop(['Date_added'], axis=1)
sp500companies = sp500companies.set_index(['Ticker'])
# print(sp500companies.head(10))
#
# start = pd.to_datetime('2009-01-01')
# end = pd.to_datetime('2017-01-01')
# source = 'google'
#
# for company in sp500companies.index:
#     try:
#         price_data = pdr.DataReader(company,source,start,end)
#         price_data.to_csv("../data/company_price-1/%s_adj_close.csv" % company)
#     except:
#         logging.error("Oops! %s occured for %s. \nMoving on to next entry." % (sys.exc_info()[0], company))
for company in sp500companies.index:
     try:
         companies.append(company)
     except:
         logging.error("Oops! %s occured for %s. \nMoving on to next entry." % (sys.exc_info()[0], company))

