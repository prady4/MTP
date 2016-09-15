import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#pre-process
mandi = pd.read_csv("azadpur.csv")
mandi.drop(mandi.columns[[0,1,2,3,4,5,6]], axis=1, inplace=True)
mandi.columns = ["price", "dod"]
mandi["dod"] =  pd.to_datetime(mandi['dod'], format='%d %b %Y')
mandi = mandi.sort(["dod"], ascending = True)


ws = pd.read_csv("WS.csv")
ws.columns = ["dod", "mid", "arrival", "origin", "var", "min", "max", "price"]
ws.drop(ws.columns[[1,2,3,4,5,6]], axis=1, inplace=True)

temp = mandi.drop_duplicates(cols='dod', take_last=True)

data = ws
for c in mandi.ix[:,0]:
	f = data[data["mid"] == c]
	f.drop(f.columns[[1,3,4,5,6]], axis=1, inplace=True)
	f = f[f["dod"] >= "2006-01-01"]
	f = f[f["dod"] <= "2015-06-23"]
	g = f.drop_duplicates(cols='dod', take_last=True)
	if len(g) > 500 and len(g) < 1000 and c!=435:
		break
