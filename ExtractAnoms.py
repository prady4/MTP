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
	a = []
	'''
	ewma = pd.ewma(residual, span=days)
	for i in range(1, 3461):
		if residual.ix[i] >= factor*ewma.ix[i]:
			anomList.append(i)
	'''
	for i in range(1, 3461):
		if i < days:
			if residual.ix[i] > factor*residual[0:i-1].mean():
				anomList.append(i)
			a.append(factor*residual[0:i-1].mean())
		else:
			if residual.ix[i] >= factor*residual[i-days:i].mean():
				anomList.append(i)
			a.append(factor*residual[i-days:i].mean())
	plt.plot(a)
	#'''
	return anomList

#New
def MovingWndw(ts1, ts2, factor, days):
	anomList = []
	a = []
	for i in range(1, 3461):
		if i < days:
			if ts2.ix[i] > factor*ts1[0:i].mean():
				anomList.append(i)
			a.append(ts1[0:i].mean())
		else:
			if residual.ix[i] >= factor*ts1[i-days:i].mean():
				anomList.append(i)
			a.append(residual[i-days:i].mean())	
	plt.plot(a,'k')
	return anomList

#df.plot()
anomList = MovingWndw(retail.ix[:,index], df[0], 1.01, 3)
def tmp(tmp1):
	indi = df[df[1] >= tmp1].index.tolist()
	indi1 = df[df[1] <= -tmp1].index.tolist()
	for i in indi:
		plt.axvline(x=i, color='r')
	for i in indi1:
		plt.axvline(x=i, color='g')
	plt.plot(retail["DELHI"], 'k')
	plt.show()

tmp(200)	#df[1].mad()

def tmp(tmp1):
	indi = df[df[1] >= tmp1].index.tolist()
	#indi1 = df[df[1] <= -tmp1].index.tolist()
	'''
	for i in indi:
		plt.axvline(x=i, color='r')
	'''
	x = windows(indi, 10)
	for i in x['start']:
		plt.axvline(x=i, color='r')
	for i in x['end']:
		plt.axvline(x=i, color='b')
	plt.plot(retail["DELHI"], 'k')
	plt.show()

tmp(1.4*df[1].mad())

def tmp(tmp1):
	indi = df[df[1] >= tmp1].index.tolist()
	#indi1 = df[df[1] <= -tmp1].index.tolist()
	for i in indi:
		plt.axvline(x=i, color='c')
	plt.plot(retail["DELHI"], 'k')
	labels = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
	d = [i*365 for i in range(1,10)]
	plt.xlabel("Days", fontsize=20)
	plt.ylabel("Prices", fontsize=20)
	plt.legend(loc='best')
	plt.xticks(d, labels, rotation='vertical', fontsize=20)
	plt.yticks(fontsize=20)
	plt.title("Anomalies", fontsize=20)
	plt.grid()
	plt.show()
	plt.show()

tmp(1.4*df[1].mad())

'''
	x = windows(indi, days)
	for i in x['start']:
		plt.axvline(x=i, color='r')
	for i in x['end']:
		plt.axvline(x=i, color='b')
'''
MovingWndw(retail["DELHI"], 1.25, 7)
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
			if (end - start) >= 6:
				s.append(start)
				e.append(end)
		elif (anomList[i] - anomList[i-1]) < wndwSize:
			end = anomList[i]
		elif (anomList[i] - anomList[i-1]) > wndwSize:
			if (end - start) >= 6:
				s.append(start)
				e.append(end)
				start = anomList[i]
				end = anomList[i]
	return {'start': s, 'end': e}

def Plot_ICs(S_):
	labels = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
	d = [i*365 for i in range(1,10)]
	plt.figure(1)
	plt.subplot(211)
	plt.plot(S_.T[0], label="IC1")
	plt.legend(loc='best')
	plt.xticks(d, labels, rotation='vertical', fontsize=20)
	plt.grid()
	plt.subplot(212)
	plt.plot(S_.T[1], label="IC2")
	plt.legend(loc='best')
	plt.xticks(d, labels, rotation='vertical', fontsize=20)
	plt.grid()
	plt.show()
	return

def rc_signal(index, S_, A_, X):
	plt.plot(X.ix[:,index-1], 'b', label="DELHI")
	plt.plot(np.dot(S_,A_[index-1].T), 'r', label="Reconstructed Singal")
	labels = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
	d = [i*365 for i in range(1,10)]
	plt.xlabel("Days", fontsize=20)
	plt.ylabel("Prices", fontsize=20)
	plt.legend(loc='best')
	plt.xticks(d, labels, rotation='vertical', fontsize=20)
	plt.yticks(fontsize=20)
	plt.title("Reconstructed Signals", fontsize=20)
	plt.grid()
	plt.show()
	return

def IC_contribution(index, S_, A_, X):
	centre_name = ["BHUBANESHWAR", "DELHI", "LUCKNOW", "MUMBAI", "PATNA"]
	plt.clf()
	plt.figure(figsize=(1900/100, 1000/100), dpi=100)
	#plt.plot(X.ix[:,index-1], 'k', label=centre_name[index-1])
	plt.plot(np.dot(S_,A_[index-1].T), 'k', label="Reconstructed Singal")
	plt.plot(S_.T[0]*A_[index-1][0], 'r', label='IC1')
	plt.plot(S_.T[1]*A_[index-1][1], 'c', label='IC2')
	plt.title('Contribution of ICs for '+str(centre_name[index-1]))
	plt.xlabel("Days", fontsize=20)
	plt.ylabel("Prices", fontsize=20)
	plt.legend(loc='best')
	plt.xticks(d, labels, rotation='vertical', fontsize=20)
	plt.yticks(fontsize=20)
	plt.grid()
	#plt.show()
	plt.savefig('Contribution of ICs for '+str(centre_name[index-1]))
	return

def ICA(index, wndwSizeMA, factor, wndwSize):
retail = pd.read_csv("processed_retail.csv")
X = retail.ix[:,1:6]
ica = FastICA(n_components=2)
S_ = ica.fit_transform(X)
A_ = ica.mixing_
'''
#Plot_ICs(index, S_)					#Plots ICs
#rc_signal(index, S_, A_, X)			#Reconstruction of signal
IC_contribution(index, S_, A_, X)		#Plot contribution of individual anomaly
return
ICA(2, 11, 0.75, 11)
#'''
#extract Anoms
df = pd.DataFrame()
df[0] = np.dot(S_,A_[index-1].T) + ica.mean_[index-1]
df[1] = (retail.ix[:,index] - df[0])
#configure Factor
df.plot()
anomList = MovingWndw(retail.ix[:,index], df[0], factor, wndwSizeMA)
plt.show()
	print("Number of anoms in ICA: "+str(len(anomList)))
	'''
	residual = analyze_diff(index)
	anomList1 = MovingWndw(residual, 1.25, wndwSizeMA)
	print("Number of anoms naturally: "+str(len(anomList1)))
	#x = list(set(anomList1) - set(anomList))
	print(len(x))
	'''
	df[3] = df[0] - ica.mean_[index-1]
	labels = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
	d = [i*365 for i in range(1,10)]
	#'''
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
	#plt.plot(df[0], 'r')
	plt.grid()
	plt.show()
	return

'''
#ICA(index, wndwSizeMA, factor, wndwSize(create periods))
ICA(2, 7, 1.50, 7)
for i in range(1,6):
	ICA(i, 7, 1.10, 7)
'''

'''
index for all the centres are as Follows:
1: BHUBANESHWAR
2: DELHI
3: LUCKNOW
4: MUMBAI
5: PATNA
'''

