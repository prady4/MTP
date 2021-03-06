import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

from sklearn.svm import SVC


def cleaning():
	#if start

def online_predictor(X, y, days, index):
	retail = pd.read_csv("processed_retail.csv")
	data = retail.ix[:,index]
	#read X for input and y for label
	#also, incorporate days into training.
	clf = SVC()
	clf.fit(X, y)
	anomList = []
	bnomList = []
	for i in range(0, len(data) - days + 1):
		x = data[i:i+days-1]
		df = pd.DataFrame()
		df.set_value(0, 0, x.mean())
		df.set_value(0, 1, x.skew())
		df.set_value(0, 3, max(x))
		df.set_value(0, 4, min(x))
		if max(x) == min(x):
			df.set_value(0, 2, 0)
		else:
			df.set_value(0, 2, x.kurtosis())
		df.set_value(0, 5, len(signal.find_peaks_cwt(x, np.arange(1,10))))
		tmp = x/x.shift(3)
		tmp = tmp.fillna(0)
		df.set_value(0, 6, max(tmp))
		df.set_value(0, 7, min(tmp))
		if clf.predict(df)[0] == 1:
			anomList.append(i)
		else:
			bnomList.append(i)
	return anomList

plt.plot(retail["DELHI"])
for i in bnomList:
	plt.axvline(x=i, color='r')

plt.show()
#0: mean
#1: skewness
#2: kurtosis
#3: minimum
#4: maximum
#5: peaks
#6: maximum rate of increase
#7: maximum rate of decrease --> Need Improvement

#s and e are anomaly indices
#s = [3, 325, 345, 401, 421, 594, 636, 674, 1018, 1046, 1370, 1395, 1426, 1499, 1544, 1776, 1915, 1955, 2080, 2235, 2558, 2602, 2680, 2755, 2775, 2803, 2833, 2917, 3072, 3113, 3145, 3230, 3264, 3444]
#e = [36, 332, 379, 408, 549, 616, 653, 716, 1038, 1095, 1387, 1416, 1449, 1508, 1712, 1891, 1933, 2025, 2185, 2302, 2593, 2613, 2725, 2767, 2795, 2822, 2909, 2964, 3104, 3123, 3221, 3244, 3434, 3460]
feature = pd.DataFrame()
for i in range(0, len(s)):
	x = retail["DELHI"].ix[s[i]:e[i]]
	feature.set_value(i, 0, x.mean())
	feature.set_value(i, 1, x.skew())
	feature.set_value(i, 3, max(x))
	feature.set_value(i, 4, min(x))
	if max(x) == min(x):
		feature.set_value(i, 2, 0)
	else:
		feature.set_value(i, 2, x.kurtosis())
	feature.set_value(i, 5, len(signal.find_peaks_cwt(x, np.arange(1,10))))
	tmp = x/x.shift(3)
	tmp = tmp.fillna(0)
	feature.set_value(i, 6, max(tmp))
	feature.set_value(i, 7, min(tmp))

for i in range(0, len(e)):
	if i == len(e)-1:
		if e[i] == 3460:
			break
		else:
			x = retail["DELHI"].ix[e[i]:3460]
	else:
		x = retail["DELHI"].ix[e[i]:s[i+1]-1]
	feature.set_value(i+34, 0, x.mean())
	feature.set_value(i+34, 1, x.skew())
	feature.set_value(i+34, 3, max(x))
	feature.set_value(i+34, 4, min(x))
	if max(x) == min(x):
		feature.set_value(i+34, 2, 0)
	else:
		feature.set_value(i+34, 2, x.kurtosis())
	feature.set_value(i+34, 5, len(signal.find_peaks_cwt(x, np.arange(1,10))))
	tmp = x/x.shift(3)
	tmp = tmp.fillna(0)
	feature.set_value(i+34, 6, max(tmp))
	feature.set_value(i+34, 7, min(tmp))

#labels
l = [1 for x in range(0,34)]
l1 = [-1 for x in range(0,33)]
labels = l+l1

online_predictor(feature, labels, 10, 2)

#list of sets
anom_set = []
for i in range(0,len(s)):
	anom_set.append(set(np.arange(s[i], e[i]+1)))

#list of sets
anom_set = []
for i in range(0,len(aa)):
	anom_set.append(set(np.arange(aa[i]-6, aa[i]+1)))

#creating training set using timeseries only
train = pd.DataFrame()
train_label = pd.DataFrame(np.zeros((3454, 1)))
retail = pd.read_csv("processed_retail.csv")
data = retail.ix[:,2]
for i in range(6, 3461):
	train[i-6] = data.ix[i-6:i].reset_index(drop=True)
	train_label.ix[i-6] = 0
	for ele in anom_set:
		if i in ele:
			train_label.ix[i-6] = 1
			break


train.tranpose()

#creatning training set using statistical features
train = pd.DataFrame(np.zeros((3454, 7)))
retail = pd.read_csv("processed_retail.csv")
#index = 2 for Delhi
data = retail.ix[:,2]
for i in range(6, 3461):
	x = data.ix[i-6:i]
	train.ix[i-6,0] = x.mean()
	train.ix[i-6,1] = x.skew()
	train.ix[i-6,2] = x.max()
	train.ix[i-6,3] = x.min()
	if max(x) != min(x):
		train.ix[i-6,4] = x.kurtosis()
	train.ix[i-6,5] = len(signal.find_peaks_cwt(x, np.arange(1,10)))
	tmp = x/x.shift(3)
	tmp = tmp.fillna(0)
	train.ix[i-6,6] = max(tmp)
	train.ix[i-6,7] = min(tmp)