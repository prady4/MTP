import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#pre-process
mandi = pd.read_csv("mandis.csv")
mandi.columns = ["mid", "mname", "scode", "lati", "long", "cid"]
ws = pd.read_csv("WS.csv")
ws.columns = ["dod", "mid", "arrival", "origin", "var", "min", "max", "price"]
data = ws
data.drop(data.columns[[3,4,5,6]], axis=1, inplace=True)
data = data.sort(["mid"], ascending = True)

for c in mandi.ix[:,0]:
	f = data[data["mid"] == c]
	#f.drop(f.columns[[1,3,4,5,6]], axis=1, inplace=True)
	f = f[f["dod"] >= "2006-01-01"]
	f = f[f["dod"] <= "2015-06-23"]
	if len(f) > 2300:
		break

f = f.drop_duplicates(cols='dod', take_last=True)
f['dod'] =  pd.to_datetime(f['dod'], format='%Y-%m-%d')
f.set_index('dod', inplace=True)
idx = pd.date_range('2006-01-01', '2015-06-23')
f = f.reindex(idx, fill_value=0)
f.reset_index(level=0, inplace=True)
f.columns = ["dod","mid", "arrival", "price"]

f["dod"] = f["dod"].dt.dayofweek
non= []
for i in range(0,7):
	h = f[f["dod"] == i]
	non.append(len(h[h["price"] == 0]))
	
f.drop(data.columns[[0,1,2]], axis=1, inplace=True)

for i in range(2006, 2016):
	h = f.ix[datetime.date(year=i,month=1,day=1):datetime.date(year=i,month=12,day=31)]
	plt.plot(h)
	if i%2 != 0:
		plt.show()
