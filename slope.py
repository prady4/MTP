import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#read CSVs
mandi = pd.read_csv("subset_mandi.csv")
centres = pd.read_csv("subset_centres.csv")
data = pd.read_csv("subset_retail.csv")
ws = pd.read_csv("subset_ws.csv")

ws['date'] =  pd.to_datetime(ws['date'], format='%Y-%m-%d')

a = ws[ws['mid']==11]
b = ws[ws['mid']==35]

idx = pd.date_range('2006-01-01', '2015-06-23')
a.set_index('date', inplace=True)
a = a.reindex(idx, fill_value=0)
a.reset_index(level=0, inplace=True)

b.set_index('date', inplace=True)
b = b.reindex(idx, fill_value=0)
b.reset_index(level=0, inplace=True)

#a = series1
a.reset_index(inplace=True)

#b = series2
b.reset_index(inplace=True)

a['price'] = pd.ewma(a['price'], span=7)
b['price'] = pd.ewma(b['price'], span=7)

df = a.head(len(a)-7)
#df.reset_index('index', inplace=True)


df['slope'] = df.apply(lambda x: 0 if ((b.ix[x['level_0']+7]['price'] - b.ix[x['level_0']]["price"])*x['price'] == 0) else (((a.ix[x['level_0']+7]['price'] - x['price'])*b.ix[x['level_0']]["price"])/((b.ix[x['level_0']+7]['price'] - b.ix[x['level_0']]["price"])*x['price'])), axis=1)

med = df["slope"].median()
tolerance = (med -df["slope"]).median()*1.4826
threshold_P = med + tolerance
threshold_N = med - tolerance
pos_slope = df[df['slope'] > threshold_P]
neg_slope = df[df['slope'] < threshold_N]

#a = pos_slope.reindex(range(0,3454),fill_value=0)
x = pos_slope.index.tolist()
for i in x:
	plt.axvline(x=i)
plt.show()
#plt.plot(a["slope"])
