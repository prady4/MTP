import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#read CSVs
mandi = pd.read_csv("mandis.csv")
centres = pd.read_csv("centres.csv")
data = pd.read_csv("Retail.csv", header=None)
ws = pd.read_csv("WS.csv", header=None)
#add headers
mandi.columns = ["mid", "mandi_name", "state_code", "latitude", "longitude", "cid"]
ws.columns = ["date", "mid", "arrival", "origin", "var", "min_price", "max_price", "price"]
data.columns = ["date","cid","price"]

#prune acc to dates
data = data[data["date"] >= "2006-01-01"]
data = data[data["date"] <= "2015-06-23"]

ws = ws[ws["date"] >= "2006-01-01"]
ws = ws[ws["date"] <= "2015-06-23"]

#prune prices
data = data[data["price"] != 0]
ws = ws[ws["price"] != 0]
ws = ws[ws["arrival"] != 0]

#drop cols
ws.drop(ws.columns[[3,4,5,6]], axis=1, inplace=True)
ws.dropna(inplace=True)

#sorting
ws = ws.sort(["date"], ascending = True)
data = data.sort(["date"], ascending = True)


'''
data['date'] =  pd.to_datetime(data['date'], format='%Y-%m-%d')
data['day'] = data['date'].dt.dayofweek
data = data[(data["day"] != 6) & (data["day"] != 5)]

ws['date'] =  pd.to_datetime(ws['date'], format='%Y-%m-%d')
ws['day'] = ws['date'].dt.dayofweek
ws = ws[(ws['day'] != 6) & (ws['day'] != 5)]
'''


#centres with mandi and enough data
centres_s = []
mandi_s = []
mid = []

i = 0
for i in range(1,77):
	f = data[data["cid"] == i]
	f = f.drop_duplicates(subset='date', take_last=True)
	if len(f) > 1977:
		centres_s.append(i)
		mid.append([])
		count = 0
		d = mandi[mandi["cid"] == i]
		e = d.ix[:,0]
		for x in e:
			f = ws[ws["mid"] == x]
			f = f.drop_duplicates(subset='date', take_last=True)
			if len(f) > 1977:
				count = count + 1
				mid[len(mid)-1].append(x)
		i = i + 1
		mandi_s.append(count)


pairs = []
for i in range(0,len(centres_s)):
	if mandi_s[i] >= 3:
		#pairs.append(centres_s[i])
		pairs = pairs+mid[i]


centres.set_index('cid', inplace=True)
india = pd.read_csv("ii.csv", header=None)

plt.plot(india[0], india[1], 'k')
plt.plot(xx['longitude'], xx['latitude'],'co', label='Mandis')
plt.plot(yy['long'], yy['lat'],'ro', label='Centres')
plt.legend('upper left')
plt.show()

ws.set_index('mid', inplace=True)
ws.to_csv('mandi_subset.csv')
