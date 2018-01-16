import  numpy as np
import  pandas as pd

s = pd.Series([1,2,3,4,5,6,6])

# print s
# print s.index

dates = pd.date_range('20180101',periods=31)
# print dates

df = pd.DataFrame(np.random.randn(31, 4), index=dates, columns=list('ABCD'))
# print df.head()
# print df.tail()
# print df.index
# print df.values
# print df.sort_index(axis=0, ascending=False)
# print df[list('AC')]
# print df[:3]
# print df.loc[:,list('AC')]
# print df.iloc[1,1]
# print df.iloc[1,:]