#! /usr/bin/python
#-*-coding:utf-8 -*-

import numpy as np
import pandas as pd

myarray =  np.array([[1,2,3],[4,5,6]])
rownames = ['a','b']
clonames = ['one','two','three']
mydataframe = pd.DataFrame(myarray,index=rownames,columns=clonames)
print(mydataframe)
