import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#pre-process
mandi = pd.read_csv("mandis.csv") #, header=None
mandi.columns = ["mid", "mname", "scode", "lati", "long", "cid"]
ws = pd.read_csv("WS.csv", header=None)
ws.columns = ["date", "mid", "arrival", "origin", "var", "min", "max", "price"]

def no_days_mandis(centreid):
	d = mandi[mandi["cid"] == centreid]
	d = d.reset_index()
	d.drop(d.columns[[0]], axis=1, inplace=True)
	d.columns = ["mid", "mname", "days", "lati", "long", "cid"]
	for i in range(0, len(d)):
		f = ws[ws["mid"] == d["mid"][i]]
		f.drop(f.columns[[1,3,4,5,6]], axis=1, inplace=True)
		f = f[f["date"] >= "2006-01-01"]
		f = f[f["date"] <= "2015-06-23"]
		f = f.sort(["date"], ascending = True)
		f = f.drop_duplicates(cols='date', take_last=True)
		d["days"][i] = len(f)
	return d

for c in range(1,77):
	d = mandi[mandi["cid"] == c]
	e = d.ix[:,0]
	for x in e:
		f = ws[ws["mid"] == 474]
		f.drop(f.columns[[1,3,4,5,6]], axis=1, inplace=True)
		f = f[f["date"] >= "2006-01-01"]
		f = f[f["date"] <= "2015-06-23"]
		f = f.sort(["date"], ascending = True)
		f = f.drop_duplicates(cols='date', take_last=True)
		f['date'] =  pd.to_datetime(f['date'], format='%Y-%m-%d')
		f.set_index('date', inplace=True)
		idx = pd.date_range('2006-01-01', '2015-06-23')
		f = f.reindex(idx, fill_value=0)
		f = f.reset_index() #level=0, inplace=True
		f.columns = ["date","arrival", "price"]
		nc[c].append(len(f[f["price"] == 0]))
		
		
plt.bar(range(0,len(nc[15])), nc[15])
plt.show()


#mandi vs entries hist
#mandis count for data count hist

nv = np.arange(1581)
data = ws
data.drop(data.columns[[3,4,5,6]], axis=1, inplace=True)
data = data.sort(["mid"], ascending = True)


for c in mandi.ix[:,0]:
	f = data[data["mid"] == c]
	#f.drop(f.columns[[1,3,4,5,6]], axis=1, inplace=True)
	f = f[f["date"] >= "2006-01-01"]
	f = f[f["date"] <= "2015-06-23"]
	g = f.drop_duplicates(cols='date', take_last=True)
	nv[c-1] = len(g)

x_labels = np.arange(36)
bins = np.linspace(0, 3500, 18)
plt.hist(nv, bins, align='left')
plt.xlabel("DATA PRESENT-CHUNK SIZE 200")
plt.ylabel("NUMBER OF MANDIS")
plt.title("Histogram of number of Entries")
plt.xticks(bins[::-1])
plt.grid()
plt.show()

#PLOT NUMBER OF ENTRIES VS NUMBER OF MANDIS
a = sorted(nv, reverse = True)
plt.plot(a)
plt.xlabel("NUMBER OF MANDIS")
plt.ylabel("NUMBER OF ENTRIES")
plt.title("DISTRIBUTION OF DATA AMONG MANDIS")
plt.grid()
plt.show()




'''
#histogram for particular mandis
nc = [[] for i in range(0,76)]
d = mandi[mandi["cid"] == 1]
e = d.ix[:,0]
for x in e:
	f = ws[ws["mid"] == x]
	f.drop(f.columns[[1,3,4,5,6]], axis=1, inplace=True)
	f = f[f["date"] >= "2006-01-01"]
	f = f[f["date"] <= "2015-06-23"]
	f = f.sort(["date"], ascending = True)
	f = f.drop_duplicates(cols='date', take_last=True)
	print len(f)
	if len(f) > 1900:
		f['date'] =  pd.to_datetime(f['date'], format='%Y-%m-%d')
		f.set_index('date', inplace=True)
		idx = pd.date_range('2006-01-01', '2015-06-23')
		f = f.reindex(idx, fill_value=0)
		f.reset_index(level=0, inplace=True)
		f.columns = ["date","arrival", "price"]
		f["price"] = pd.ewma(f["price"], span=70)
		plt.plot(f["price"])
		plt.xticks([260, 520, 780, 1040, 1300, 1560, 1820, 2080, 2340, 2600, 2860, 3120, 3380])
		plt.grid()
		plt.show()
	#nc[44].append(len(f[f["price"] == 0]))
	

plt.bar(range(0,len(nc[44])), nc[44])
plt.show()


plt.bar(range(0,len(nl)), nl, color = 'g')
plt.bar(range(0,len(ns)), ns, color = 'b')
plt.show()

'''

#ofmandis VS #mandisWithSubstantialData In accordance to centres
nc = [[] for i in range(0,76)]

for c in range(1,77):
	d = mandi[mandi["cid"] == c]
	e = d.ix[:,0]
	for x in e:
		f = ws[ws["mid"] == x]
		f.drop(f.columns[[1,3,4,5,6]], axis=1, inplace=True)
		f = f[f["date"] >= "2006-01-01"]
		f = f[f["date"] <= "2015-06-23"]
		f = f.drop_duplicates(cols='date', take_last=True)
		if (len(f)) > 1900:
			nc[c-1].append(len(f))
		
		
ns = [0 for i in range(0,76)]
for i in range(0,76):
	x = nc[i]
	nl[i] = len(x)
	for j in x:
     		if j > 1977:
     			ns[i] = ns[i] + 1



#bins = np.linspace(0, 3500, 35)
#plt.hist(nl, bins)
#plt.hist(ns)

x_labels = np.arange(76)
plt.bar(range(0,len(nl)), nl, color = 'g', label="#Mandis Allocated")
plt.bar(range(0,len(ns)), ns, color = 'b', label="#Mandis with sufficient data")
plt.xlabel("Centres")
plt.ylabel("NUMBER OF MANDIS")
plt.title("Mandis with 80% data present")
plt.xticks(x_labels+1)
plt.legend(loc='upper right')
plt.grid()
plt.show()



#centres with mandi and enough data
cid = []
ncc = []
ncns = []

for i in range(1,77):
	f = data[data["cid"] == i]
	f = f.drop_duplicates(cols='date', take_last=True)
	if len(f) > 1900:
		cid.append(i)
		count = 0
		d = mandi[mandi["cid"] == i]
		e = d.ix[:,0]
		for x in e:
			f = ws[ws["mid"] == x]
			f.drop(f.columns[[1,3,4,5,6]], axis=1, inplace=True)
			f = f[f["date"] >= "2006-01-01"]
			f = f[f["date"] <= "2015-06-23"]
			f = f.sort(["date"], ascending = True)
			f = f.drop_duplicates(cols='date', take_last=True)
			if len(f) > 1500:
				count = count + 1
		ncc.append(count)

