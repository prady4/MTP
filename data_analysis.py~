import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#pre-process
data = pd.read_csv("Retail.csv", header=None)
#d = data.ix[:,1]
data.columns = ["date","cid","price"]


#Filling dates
d = data[data["cid"] == 16]
e = d[d["date"] >= "2006-01-01"]
e = e[e["date"] <= "2015-06-23"]
e = e.sort(["date"], ascending = True)
e = e.drop_duplicates(cols='date', take_last=True)
e['date'] =  pd.to_datetime(e['date'], format='%Y-%m-%d')
#e.drop('cid', axis=1, inplace=True)
e.set_index('date', inplace=True)
idx = pd.date_range('2006-01-01', '2015-06-23')
e = e.reindex(idx)	#Or null
#g['date'] = g.index
e.reset_index(level=0, inplace=True)
e.columns = ["date","cid","price"]


#before filling distribution
f = e.ix[:,0]
l = []
p = datetime.strptime('2006-01-01', "%Y-%m-%d")
i = 0
s = []
for q in f:
	q = datetime.strptime(q, "%Y-%m-%d")
	diff = abs(p-q).days - 1	
	if(diff > 0):
		l.append(diff)
		s.append(i)
		i = 0
	p = q
	i = i + 1


plt.plot(s,l)
plt.show()


#null counts
nc = []
for index in range(1,77):
	d = data[data["cid"] == index]
	e = d[d["date"] >= "2006-01-01"]
	e = e[e["date"] <= "2015-06-23"]
	e = e.sort(["date"], ascending = True)
	f = e.ix[:,2]
	nc.append(f.isnull().sum())

#duplicates count
dc = []
for index in range(1,77):
	d = data[data["cid"] == index]
	e = d[d["date"] >= "2006-01-01"]
	e = e[e["date"] <= "2015-06-23"]
	e = e.sort(["date"], ascending = True)
	e.drop_duplicates(cols='date', take_last=True)
	#e[e.ix[:,0].duplicated()]
	#print "\n"


#histogram
nc = []
for index in range(1,77):
	d = data[data["cid"] == index]
	e = d[d["date"] >= "2006-01-01"]
	e = e[e["date"] <= "2015-06-23"]
	e = e.sort(["date"], ascending = True)
	e = e.drop_duplicates(cols='date', take_last=True)
	e['date'] =  pd.to_datetime(e['date'], format='%Y-%m-%d')
	e.drop('cid', axis=1, inplace=True)
	e.set_index('date', inplace=True)
	idx = pd.date_range('2006-01-01', '2015-06-23')
	e = e.reindex(idx, fill_value=0)
	nc.append(len(e[e["price"] == 0]))

plt.bar(range(0,100), x)
plt.show()



#NO nulls in centre
count = 0
for i in  nc:
     if i > 3000:
             count = count + 1


count

#smoothing
pd.ewma(e, span=7)

#f.nunique()
g = f.value_counts()	#dropna = False
g['date'] = g.index
i = g
j = i.sort(["date"], ascending = True)
y = list(j.ix[:,0])
x = list(j.ix[:,1])
#j.plot()
plt.plot(x)
plt.show()

for i in range(1000,1300):
	if l[i] > 500:
		print i

f.nunique()


#new
nc = []
for index in range(1,77):
	d = data[data["cid"] == index]
	e = d[d["date"] >= "2006-01-01"]
	e = e[e["date"] <= "2015-06-23"]
	nc.append(len(e))
	
plt.plot(a)
plt.xlabel("NUMBER OF CENTRES")
plt.ylabel("NUMBER OF ENTRIES")
plt.title("DISTRIBUTION OF DATA AMONG CENTRES")
plt.grid()
plt.show()


#find nulls
nc.append(len(e[e.isnull().T.any().T]))
