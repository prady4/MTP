import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from scipy import signal
from sklearn.decomposition import FastICA, PCA

#

def analyze_diff(center_index):
	retail = pd.read_csv("processed_retail.csv")
	indices = [1,2,3,4,5]
	tmp = retail["DELHI"]*0
	indices = list(set(indices) - {center_index})
	for i in indices:
		tmp = tmp + (retail.ix[:,center_index] - retail.ix[:,i]).abs()
	tmp = tmp/4
	return tmp

#tmp = analyze_diff(2)

def MovingWndw(residual, factor, days):
	anomList = []
	ewma = pd.ewma(residual, span=days)
	for i in range(1, 3461):
		if residual.ix[i] >= factor*ewma.ix[i]:
			anomList.append(i)
	'''
	if i < days:
		if residual.ix[i] > factor*residual[0:i-1].mean():
			anomList.append(i)
	else:
		if residual.ix[i] >= factor*residual[i-days:i].mean():
			anomList.append(i)
	'''
	return anomList

def plot(index, factor, days):
	residual = analyze_diff(index)
	anomList = MovingWndw(residual, factor, days)
	for i in anomList:
		plt.axvline(x=i)
	plt.plot(residual)
	print("Number of anoms: "+str(len(anomList)))
	plt.show()
	return

for i in range(1,6):
	plot(i, 1.25, 10)
'''
index for all the centres are as Follows:
1: BHUBANESHWAR
2: DELHI
3: LUCKNOW
4: MUMBAI
5: PATNA
'''
#plot(2, 7)

def windows(anomList, wndwSize):
	s = []
	e = []
	start = anomList[0]
	end = anomList[0]
	for i in range(1,len(anomList)+1):
		if i == len(anomList):
			if (end - start) != 0:
				s.append(start)
				e.append(end)
		elif (anomList[i] - anomList[i-1]) < wndwSize:
			end = anomList[i]
		elif (anomList[i] - anomList[i-1]) > wndwSize:
			if (end - start) != 0:
				s.append(start)
				e.append(end)
				start = anomList[i]
				end = anomList[i]
	return {'start': s, 'end': e}

def ICA(index, wndwSizeMA, factor, wndwSize):
	centre_name = ["BHUBANESHWAR", "DELHI", "LUCKNOW", "MUMBAI", "PATNA"]
	retail = pd.read_csv("processed_retail.csv")
	X = retail.ix[:,1:6]
	ica = FastICA(n_components=2)
	S_ = ica.fit_transform(X)
	A_ = ica.mixing_
	'''
	plt.plot(retail["DELHI"], 'g')
	plt.plot(np.dot(S_,A_[2].T) + ica.mean_[2], 'r')
	plt.show()
	'''
	df = pd.DataFrame()
	df[0] = np.dot(S_,A_[index-1].T) + ica.mean_[index-1]
	df[1] = (retail.ix[:,index] - df[0]).abs()
	#configure Factor
	anomList = MovingWndw(df[1], factor, wndwSizeMA)
	print("Number of anoms in ICA: "+str(len(anomList)))
	residual = analyze_diff(index)
	anomList1 = MovingWndw(residual, 1.25, wndwSizeMA)
	print("Number of anoms naturally: "+str(len(anomList1)))
	x = list(set(anomList1) - set(anomList))
	print(len(x))
	df[3] = df[0] - ica.mean_[index-1]
	labels = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
	d = [i*365 for i in range(1,10)]
	'''
	Plot contribution of individual anomaly
	plt.clf()
	plt.figure(figsize=(1900/100, 1000/100), dpi=100)
	plt.plot(retail.ix[:,index], 'r', label=centre_name[index-1])
	plt.plot(S_.T[0]*A_[index-1][0] + ica.mean_[index-1]/2, 'c', label='IC1')
	plt.plot(S_.T[1]*A_[index-1][1] + ica.mean_[index-1]/2, 'y', label='IC2')
	plt.title('Contribution of ICs for '+str(centre_name[index-1]))
	plt.xlabel("Days")
	plt.ylabel("Prices")
	plt.legend(loc='best')
	plt.xticks(d, labels, rotation='vertical')
	plt.grid()
	plt.savefig('Contribution of ICs for '+str(centre_name[index-1]))
	'''
	'''
	#Plot points reported as anomaly
	for i in anomList:
		plt.axvline(x=i, color='r')
	for i in anomList1:
		plt.axvline(x=i, color='b')
	'''
	'''
	#Create periods of anomaly
	'''
	x = windows(anomList, wndwSize)
	for i in x['start']:
		plt.axvline(x=i, color='r')
	for i in x['end']:
		plt.axvline(x=i, color='b')
	#'''
	plt.plot(retail.ix[:,index], 'g')
	plt.plot(df[0], 'r')
	plt.grid()
	plt.show()
	return

'''
#ICA(index, wndwSizeMA, factor, wndwSize(create periods))
ICA(2, 11, 0.75, 11)
for i in range(1,6):
	ICA(i, 11, 0.9, 11)
'''

'''
index for all the centres are as Follows:
1: BHUBANESHWAR
2: DELHI
3: LUCKNOW
4: MUMBAI
5: PATNA
'''

