import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#read CSVs
mandi = pd.read_csv("subset_mandi.csv")
centres = pd.read_csv("subset_centres.csv")
data = pd.read_csv("subset_retail.csv")
ws = pd.read_csv("subset_ws.csv")



#intermediate_results
mandi_id = [11, 35, 31, 182, 174, 194, 281, 404, 351, 312, 165, 70, 293, 164, 447, 407, 166, 345, 337, 577, 545, 323, 405, 284, 324, 584, 285, 278, 288, 325, 279, 376, 156, 427]
cid = [3, 10, 16, 37, 40, 44, 50]
mandi_s = [0, 3, 1, 0, 3, 0, 11, 0, 0, 1, 1, 3, 9, 2, 3, 0, 0, 0, 0]
centres_s = [1, 3, 7, 9, 10, 12, 16, 23, 27, 31, 32, 37, 40, 44, 50, 54, 61, 62, 68]
mid = [[], [11, 35, 31], [109], [], [182, 174, 194], [], [281, 404, 351, 312, 165, 70, 293, 164, 447, 407, 166], [], [], [394], [89], [345, 337, 577], [545, 323, 405, 284, 324, 584, 285, 278, 288], [156, 427], [325, 279, 376], [], [], [], []]


ws['date'] =  pd.to_datetime(ws['date'], format='%Y-%m-%d')
ws.set_index('date', inplace=True)
idx = pd.date_range('2006-01-01', '2015-06-23')
m = m.reindex(idx, fill_value=0)
m.reset_index(level=0, inplace=True)


'''
data['date'] =  pd.to_datetime(data['date'], format='%Y-%m-%d')
data['day'] = data['date'].dt.dayofweek
data = data[(data["day"] != 6) and (data["day"] != 5)]

ws['date'] =  pd.to_datetime(ws['date'], format='%Y-%m-%d')
ws['day'] = ws['date'].dt.dayofweek
ws = ws[(ws["day"] != 6) and (ws["day"] != 5)]

#No weekends, Threshold 80%
centres_s = [1, 3, 7, 9, 10, 12, 16, 23, 27, 31, 32, 37, 40, 44, 50, 54, 61, 62, 68]
mandi_s = [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0]
mid = [[], [], [], [], [], [], [312, 164, 166], [], [], [], [], [], [278, 288], [], [279], [], [], [], []]

#No weekends, Threshold 60%
centres_s = [1, 3, 4, 5, 7, 9, 10, 11, 12, 15, 16, 23, 27, 31, 32, 37, 40, 41, 44, 50, 54, 56, 61, 62, 64, 68]
mandi_s = [0, 3, 0, 3, 1, 0, 2, 10, 0, 2, 12, 0, 0, 1, 1, 3, 10, 20, 4, 2, 0, 4, 0, 1, 0, 0]
mid = [[], [11, 35, 31], [], [261, 259, 223], [109], [], [182, 194], [232, 241, 204, 210, 256, 507, 726, 200, 206, 234], [], [318, 459], [281, 404, 351, 312, 165, 70, 293, 164, 447, 758, 407, 166], [], [], [394], [89], [345, 337, 577], [295, 545, 323, 405, 284, 324, 584, 285, 278, 288], [225, 215, 203, 219, 202, 227, 198, 205, 222, 389, 246, 434, 231, 492, 213, 218, 238, 254, 245, 237], [163, 427, 146, 148], [325, 279], [], [99, 106, 93, 342], [], [86], [], []]



new_id = [31, 182, 174, 194, 281, 404, 351, 165, 70, 293, 164, 407, 166, 577, 545, 323, 405, 584, 278, 288, 279, 376]
new_cid = = [10, 16, 40, 44, 50]
mid_id = [[182, 174, 194], [281, 404, 351, 312, 165, 70, 293, 164, 407, 166], [545, 323, 405, 584, 278, 288], [156, 427], [279, 376]]
'''



for i in mandi_id:
	a = ws[ws["mid"]==i]
	a["arrival"].max()
#plots

ws['date'] =  pd.to_datetime(ws['date'], format='%Y-%m-%d')
new = pd.DataFrame()
new_id = []
for i in cid_id:
	m = data[data["cid"] == i]
	m = m[m["date"] >= "2006-01-01"]
	m = m[m["date"] <= "2015-06-23"]
	m = m.drop_duplicates(cols='date')
	m['date'] =  pd.to_datetime(m['date'], format='%Y-%m-%d')
	m.set_index('date', inplace=True)
	m = m.reindex(idx)
	m["cid"] = i
	m = m.interpolate(method='pchip')
	m.reset_index(level=0, inplace=True)
	plt.plot(m["price"])
	#plt.show()
	new = new.append(m)
	
'''
all_32 = pd.DataFrame()
#new_id = []
for i in mandi_id:
	m = ws[ws["mid"] == i]
	m.set_index('date', inplace=True)
	m = m.reindex(idx)
	m["mid"] = i
	m = m.interpolate(method='pchip')
	m.reset_index(level=0, inplace=True)
	#print m["price"].isnull().sum()
	all_32 = all_32.append(m)

for i in mandi_id:
	m = all_32[all_32["mid"] == i]
	print((i,m["price"].isnull().sum()))

for i in new_id:
	m = new[new["mid"] == i]
	m = m.interpolate(method='pchip')
	if m["price"].isnull().sum() == 0:
		print(i)

for i in range(0, len(centres_s)):
     j =  mid[i]
     for k in j:
             if k in s:
		print(centres_s[i])


m = m.reindex(idx)
m = m.interpolate(method='pchip')
'''
#centres
m = ws[ws["mid"] == 427]
m = m.drop_duplicates(cols='date')
m['date'] =  pd.to_datetime(m['date'], format='%Y-%m-%d')
m.set_index('date', inplace=True)
m = m.reindex(idx)
m["mid"] = 427
m = m.interpolate(method='pchip')
m.reset_index(level=0, inplace=True)

cid = [3, 10, 16, 37, 40, 44, 50]
#centres
c = data[data["cid"]==40]
c = c.drop_duplicates(cols='date')
c['date']=pd.to_datetime(c['date'], format='%Y-%m-%d')
c.set_index('date', inplace=True)
c = c.reindex(idx)
c = c.interpolate(method='pchip')

c1 = data[data["cid"]==50]
c1 = c1.drop_duplicates(cols='date')
c1['date']=pd.to_datetime(c1['date'], format='%Y-%m-%d')
c1.set_index('date', inplace=True)
c1 = c1.reindex(idx)
c1 = c1.interpolate(method='pchip')
a = sm.tsa.ccf(c1["price"], c1["price"])

a = sm.tsa.ccf(c["price"], c1["price"])
plt.plot(a)
plt.grid()
plt.show()



labels = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
d = [i*365 for i in range(0,11)]
plt.plot(m2["arrival"]*10)
plt.title("Arrival Time Series Plot")
plt.xlabel("Arrival in Quintals")
plt.ylabel("Year")
plt.xticks(d, labels, rotation='vertical')
plt.show()

labels = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
d = [i*365 for i in range(1,10)]
plt.plot(m2["price"])
plt.title("Price Time Series Plot")
plt.xlabel("Price")
plt.ylabel("Year")
plt.xticks(d, labels, rotation='vertical')
plt.show()

y = sm.tsa.acf(m2["price"], nlags=3000)
plt.plot(y)
plt.title("Auto Correlation of a Mandi")
plt.xlabel("Lag in Days")
plt.ylabel("ACF")
plt.show()

y = sm.tsa.ccf(m2["price"], m2["arrival"])
plt.plot(y)
plt.title("Auto Correlation of a Mandi")
plt.xlabel("Lag in Days")
plt.ylabel("ACF")
plt.show()

plt.plot(m2["price"])
plt.plot(m2["arrival"]*10)
plt.title("Price and Arrival Plots of a Mandi")
plt.xlabel("Year")
plt.ylabel("Price/Quantity(QTL)")
plt.xticks(d, labels, rotation='vertical')
plt.show()

for i in new_id:
	m = new[new["mid"] == i]
	a = sm.tsa.ccf(m["arrival"], m["price"], unbiased=True)
	plt.plot(a)
	plt.title("Cross correlation of Arrival and Price in Mandis")
	plt.xlabel("Year")
	plt.ylabel("CCF")
	plt.xticks(d, labels, rotation='vertical')
	plt.show()






ws = pd.read_csv("WS.csv", header=None)
ws.columns = ["date", "mid", "arrival", "origin", "var", "min", "max", "price"]

mid_id = [[182, 174, 194], [281, 404, 351, 312, 165, 70, 293, 164, 407, 166], [545, 323, 405, 584, 278, 288], [!156, !427], [279, 376]]
cid_id = [10,16,40,44,50]
idx = pd.date_range('2006-01-01', '2015-06-23')


labels = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
d = [i*365 for i in range(1,10)]

for i in mid_id:
	df = pd.DataFrame()
	for j in i:
		name = 'm'+str(j)
		m = ws[ws["mid"] == j]
		m = m[m["date"] >= "2006-01-01"]
		m = m[m["date"] <= "2015-06-23"]
		m = m.drop_duplicates(cols='date')
		m['date'] =  pd.to_datetime(m['date'], format='%Y-%m-%d')
		m.set_index('date', inplace=True)
		m = m.reindex(idx)
		df[name] = m["price"]
	df["cv"] = df.std(axis=1)
	df["cv"] = df["cv"].fillna(0)
	plt.plot(df["cv"], 'c')
	plt.xlabel("Days")
	plt.ylabel("SD Price")
	plt.title("SD for centre")
	plt.xticks(d, labels, rotation='vertical')
	plt.show()


#COV Plots based on centres
data = pd.read_csv("Retail.csv", header=None)
data.columns = ["date","cid","price"]
cid_id = [10,16,40,44,50]
for i in cid_id:
	m = data[data["cid"] == i]
	m = m[m["date"] >= "2006-01-01"]
	m = m[m["date"] <= "2015-06-23"]
	m = m.drop_duplicates(cols='date')
	m['date'] =  pd.to_datetime(m['date'], format='%Y-%m-%d')
	m.set_index('date', inplace=True)
	m = m.reindex(idx)
	m = m.interpolate(method='pchip')
	plt.plot(m["price"], 'c')
	plt.show()

plt.xlabel("Days")
plt.ylabel("Prices")
plt.title("Retail of all centres")
plt.xticks(d, labels, rotation='vertical')
plt.show()

'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'sept', 'oct', 'Nov', 'Dec', 

labels = ['Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'sept', 'oct', 'Nov', 'Dec', '2007', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'sept', 'oct', 'Nov', 'Dec', '2008', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'sept', 'oct', 'Nov', 'Dec', '2009', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'sept', 'oct', 'Nov', 'Dec', '2010', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'sept', 'oct', 'Nov', 'Dec', '2011', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'sept', 'oct', 'Nov', 'Dec', '2012', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'sept', 'oct', 'Nov', 'Dec', '2013', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'sept', 'oct', 'Nov', 'Dec', '2014', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'sept', 'oct', 'Nov', 'Dec', '2015', 'Feb', 'Mar', 'Apr', 'May', 'June']
d = [i*30 for i in range(1,113)]
d = [31,28,31,30,31,30,31,31,30,31,30,31, 31,28,31,30,31,30,31,31,30,31,30,31, 31,29,31,30,31,30,31,31,30,31,30,31, 31,28,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31,31,29,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,23]
for i in d:
	e.append(i+x)
	x = e[len(e)-1]
for i in cid_id:
	c = data[data["cid"] == i]
	plt.plot(c["price"], 'c')
	plt.xlabel("Days")
	plt.ylabel("Price")
	plt.title("centre")
	plt.xticks(d, labels, rotation='vertical')

plt.show()

new_id = [31, 182, 174, 194, 281, 404, 351, 165, 70, 293, 164, 407, 166, 577, 545, 323, 405, 584, 278, 288, 279, 376]
for i in new_id:
	c = ws[ws["mid"] == i]
	plt.plot(c["price"], 'c')
	plt.xlabel("Days")
	plt.ylabel("Price")
	plt.title("centre")
	plt.xticks(d, labels, rotation='vertical')

plt.show()
