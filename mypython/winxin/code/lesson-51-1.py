# !/usr/bin/python
# -*- coding:utf-8 -*-
import os
import pandas as pd

column_names = ['Ticker', 'Security', 'GICS_Sector', 'GICS_Sub_Industry', 'Address', 'Date_added', 'CIK']
sp500companies = pd.read_csv('../data/500company.csv', header=0, names=column_names).drop(['Date_added'], axis=1)
sp500companies = sp500companies.set_index(['Ticker'])

for company in sp500companies.index:
    cmd = "scrapy crawl transcripts -a symbol="+company
    os.system(cmd)