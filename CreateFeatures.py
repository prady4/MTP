from scipy import signal
def features():
	anomalies = pd.read_csv('MumbaiGold.csv')
	ws = pd.read_csv('Mumbai.csv', header=None)
	ws[0] =  pd.to_datetime(ws[0], format='%Y-%m-%d')
	#print len(anomalies['start'])
	for i in range(0, len(anomalies['start'])):
		x = processed_retail[processed_retail['DATES'] >= datetime.datetime.strptime(anomalies['start'][i], '%d/%m/%Y').strftime('%Y-%m-%d')]
		x = x[x['DATES'] <= datetime.datetime.strptime(anomalies['end'][i], '%d/%m/%Y').strftime('%Y-%m-%d')]
		print(len(x))
	print("\n\n")
	for i in range(0, len(anomalies['start'])):
		x = processed_retail[processed_retail['DATES'] >= datetime.datetime.strptime(anomalies['start'][i], '%d/%m/%Y').strftime('%Y-%m-%d')]
		x = x[x['DATES'] <= datetime.datetime.strptime(anomalies['end'][i], '%d/%m/%Y').strftime('%Y-%m-%d')]
		peakind = signal.find_peaks_cwt(x["MUMBAI"], np.arange(1,10))
		print(len(peakind))
	print("\n\n")
	for i in range(0, len(anomalies['start'])):
		x = ws[ws[0] >= datetime.datetime.strptime(anomalies['start'][i], '%d/%m/%Y').strftime('%Y-%m-%d')]
		x = x[x[0] <= datetime.datetime.strptime(anomalies['end'][i], '%d/%m/%Y').strftime('%Y-%m-%d')]
		count = 0
		for j in range(1,len(ws.ix[0])):
			count = count + (float(sum(x[j])/len(x))*10)/max(x[j])
		print(count/(len(ws.ix[0])-1))

features()


		#print(( + (sum(x[2])/len(x)) + (sum(x[3])/len(x)))/3)

from scipy import signal
xs = np.arange(0, np.pi, 0.05)
anomalies = np.sin(xs)
peakind = signal.find_peaks_cwt(anomalies, np.arange(1,10))
peakind, xs[peakind], anomalies[peakind]


ws[0] =  pd.to_datetime(ws[0], format='%Y-%m-%d')
anomalies = pd.read_csv('anom4.tsv', sep='\t')

anom = 'anom0.tsv'
mname = 'Bhubaneshwar.csv'
"BHUBANESHWAR" = 'BHUBANESHWAR'
anomalies = pd.read_csv(anom, sep='\t')
ws = pd.read_csv(mname, header=None)
ws[0] =  pd.to_datetime(ws[0], format='%Y-%m-%d')

from sklearn.cluster import KMeans
import numpy as np
from sklearn.tree import DecisionTreeClassifier

def kmeans():
	feature = pd.read_csv("finalfeature.csv")
	kmean = KMeans(n_clusters=3, n_init=20, random_state=0).fit(feature)
	l = kmean.labels_.tolist()
	for i in l:
		print(i)

kmeans()


def DTree(x,y):
	feature = pd.read_csv("finalfeature.csv")

	test = pd.read_csv('testfeature.csv')
	temp3 = [item for item in np.arange(3461) if item not in temp2]
	clf = DecisionTreeClassifier(criterion="entropy",random_state=0)
	clf.fit(A, B)
	return clf.score(Y, Z)



anomalies = pd.read_csv('MumbaiGold.csv')
ws = pd.read_csv('Mumbai.csv', header=None)
ws[0] =  pd.to_datetime(ws[0], format='%Y-%m-%d')
for i in range(0, len(anomalies['start'])):
	x = processed_retail[processed_retail['DATES'] >= anomalies['start'][i]]
	x = x[x['DATES'] <= anomalies['end'][i]]
	print(x["MUMBAI"].mean()/x["MUMBAI"].max())

print("\n\n")
for i in range(0, len(anomalies['start'])):
	x = processed_retail[processed_retail['DATES'] >= anomalies['start'][i]]
	x = x[x['DATES'] <= anomalies['end'][i]]
	print(len(x["MUMBAI"]))

print("\n\n")
for i in range(0, len(anomalies['start'])):
	x = processed_retail[processed_retail['DATES'] >= anomalies['start'][i]]
	x = x[x['DATES'] <= anomalies['end'][i]]
	print(x["MUMBAI"].skew())

print("\n\n")
for i in range(0, len(anomalies['start'])):
	x = processed_retail[processed_retail['DATES'] >= anomalies['start'][i]]
	x = x[x['DATES'] <= anomalies['end'][i]]
	print(x["MUMBAI"].std())

print("\n\n")
for i in range(0, len(anomalies['start'])):
	x = processed_retail[processed_retail['DATES'] >= anomalies['start'][i]]
	x = x[x['DATES'] <= anomalies['end'][i]]
	peakind = signal.find_peaks_cwt(x["MUMBAI"], np.arange(1,10))
	print(len(peakind))

print("\n\n")
for i in range(0, len(anomalies['start'])):
		x = ws[ws[0] >= anomalies['start'][i]]
		x = x[x[0] <= anomalies['end'][i]]
		count = 0
		for j in range(1,len(ws.ix[0])):
			count = count + (float(sum(x[j])/len(x))*10)/max(x[j])
		print(count/(len(ws.ix[0])-1))








anomalies = pd.read_csv('LucknowGold.csv')
ws = pd.read_csv('Lucknow.csv', header=None)
ws[0] =  pd.to_datetime(ws[0], format='%Y-%m-%d')
for i in range(0, len(anomalies['start'])):
	x = processed_retail[processed_retail['DATES'] >= anomalies['start'][i]]
	x = x[x['DATES'] <= anomalies['end'][i]]
	print(x["LUCKNOW"].mean()/x["LUCKNOW"].max())

print("\n\n")
for i in range(0, len(anomalies['start'])):
	x = processed_retail[processed_retail['DATES'] >= anomalies['start'][i]]
	x = x[x['DATES'] <= anomalies['end'][i]]
	print(len(x["LUCKNOW"]))

print("\n\n")
for i in range(0, len(anomalies['start'])):
	x = processed_retail[processed_retail['DATES'] >= anomalies['start'][i]]
	x = x[x['DATES'] <= anomalies['end'][i]]
	print(x["LUCKNOW"].skew())

print("\n\n")
for i in range(0, len(anomalies['start'])):
	x = processed_retail[processed_retail['DATES'] >= anomalies['start'][i]]
	x = x[x['DATES'] <= anomalies['end'][i]]
	print(x["LUCKNOW"].std())

print("\n\n")
for i in range(0, len(anomalies['start'])):
	x = processed_retail[processed_retail['DATES'] >= anomalies['start'][i]]
	x = x[x['DATES'] <= anomalies['end'][i]]
	peakind = signal.find_peaks_cwt(x["LUCKNOW"], np.arange(1,10))
	print(len(peakind))

print("\n\n")
for i in range(0, len(anomalies['start'])):
		x = ws[ws[0] >= anomalies['start'][i]]
		x = x[x[0] <= anomalies['end'][i]]
		count = 0
		for j in range(1,len(ws.ix[0])):
			count = count + (float(sum(x[j])/len(x))*10)/max(x[j])
		print(count/(len(ws.ix[0])-1))

