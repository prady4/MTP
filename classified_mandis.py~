import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#read CSVs
mandi = pd.read_csv("subset_mandi.csv")
centres = pd.read_csv("subset_centres.csv")
data = pd.read_csv("subset_retail.csv")
ws = pd.read_csv("subset_ws.csv")

#pre process
ws['date'] =  pd.to_datetime(ws['date'], format='%Y-%m-%d')
ws.set_index('date', inplace=True)
idx = pd.date_range('2006-01-01', '2015-06-23')



#process old data
cid = [3, 10, 16, 37, 40, 50]

mid = [[], [11, 35, 31], [109], [], [182, 174, 194], [], [281, 404, 351, 312, 165, 70, 293, 164, 447, 407, 166], [], [], [394], [89], [345, 337, 577], [545, 323, 405, 284, 324, 584, 285, 278, 288], [156, 427], [325, 279, 376], [], [], [], []]

new_mid = []
for i in mid:
	if len(i) >= 3:
		new_mid.append(i)




#COV Plots based on centres
for i in range(0,len(new_mid)):
	df = pd.DataFrame()
	for j in range(0, len(new_mid[i])):
		name = 'm'+str(i)+str(j)
		m = ws[ws["mid"] == new_mid[i][j]]
		m = m.reindex(idx, fill_value=0)
		m["price"] = pd.ewma(m["price"], span=7)
		df[name] = m["price"]
	df["cv"] = df.std(axis=1)/df.mean(axis=1)
	plt.plot(df["cv"], 'c')
	plt.xlabel("Days")
	plt.ylabel("Coefficient of Variance")
	name = "Coefficient of Variance for centre :: " + centres[centres["cid"] == cid[i]]["Name"].values[0]
	plt.title(name)
	plt.show()



#Mandis Price Plots based on centres
for i in range(0,len(new_mid)):
	for j in range(0, len(new_mid[i])):
		name = 'm'+str(i)+str(j)
		m = ws[ws["mid"] == new_mid[i][j]]
		m = m.reindex(idx, fill_value=0)
		m["price"] = pd.ewma(m["price"], span=7)
		plt.plot(m["price"])
	plt.xlabel("Days")
	plt.ylabel("Price")
	name = "Price plot of mandis for centre :: " + centres[centres["cid"] == cid[i]]["Name"].values[0]
	plt.title(name)
	plt.show()



#COV across centres
df = pd.DataFrame()
for i in range(0,len(new_mid)):
	minimum = 0
	for j in range(0, len(new_mid[i])):
		temp = ws[ws["mid"] == new_mid[i][j]]
		if (len(temp) > minimum):
			m = temp
	m = m.reindex(idx, fill_value=0)
	df[i] = pd.ewma(m["price"], span=7)


df["cv"] = df.std(axis=1)/df.mean(axis=1)
plt.plot(df["cv"])
plt.xlabel("Days")
plt.ylabel("Price")
plt.title("COV plot of mandis across all centres")
plt.show()




#Mandis Price Plots accross Centres
for i in range(0,len(new_mid)):
	minimum = 0
	for j in range(0, len(new_mid[i])):
		temp = ws[ws["mid"] == new_mid[i][j]]
		if (len(temp) > minimum):
			m = temp
	m = m.reindex(idx, fill_value=0)
	plt.plot(pd.ewma(m["price"], span=7), label=centres[centres["cid"] == cid[i]]["Name"].values[0])


plt.xlabel("Days")
plt.ylabel("Price")
plt.title("Price plot of mandis across all centres")
plt.legend(loc='upper left')
plt.show()




