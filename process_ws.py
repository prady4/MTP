import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

ws = pd.read_csv("WS.csv", header=None)
ws.columns = ["date", "mid", "arrival", "origin", "var", "min", "max", "price"]
mid = [281, 404, 351, 312, 165, 70, 293, 164, 447, 407, 166]
ws.drop(ws.columns[[3,4,5,6]], axis=1, inplace=True)

d = pd.DataFrame()
for i in mid:
	f = ws[ws['mid'] == i]
	f = f[f["date"] >= "2006-01-01"]
	f = f[f["date"] <= "2015-06-23"]
	f = f.sort(["date"], ascending = True)
	f = f.drop_duplicates(cols='date', take_last=True)
	f['date'] =  pd.to_datetime(f['date'], format='%Y-%m-%d')
	f.set_index('date', inplace=True)
	idx = pd.date_range('2006-01-01', '2015-06-23')
	f = f.reindex(idx)
	f = f.reset_index()
	f = f.interpolate(method='pchip')
	d[i] = f['price']

d.to_csv('processed_ws_with_NAN.csv', index=False)
e = d.fillna(method='bfill')
e.to_csv('processed_ws.csv', index=True)