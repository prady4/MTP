import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

anom = pd.read_csv("anom1.tsv", sep='\t')
retail = pd.read_csv("processed_retail.csv")
ws = pd.read_csv("processed_ws.csv", header=None)
arrival = pd.read_csv("delhi_arrival.csv", header=None)
index = [1,3,4,12,16]
selectedAnom = anom.ix[index].reset_index()

#plot all the centres
for i in range(0, len(selectedAnom)):
	startIndex = (datetime.datetime.strptime(selectedAnom['start'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	endIndex = (datetime.datetime.strptime(selectedAnom['end'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	newFrame = retail.ix[startIndex:endIndex]
	plt.figure(1)
	plt.subplot(511)
	plt.plot(newFrame['DELHI'])
	plt.subplot(512)
	plt.plot(newFrame['LUCKNOW'])
	plt.subplot(513)
	plt.plot(newFrame['MUMBAI'])
	plt.subplot(514)
	plt.plot(newFrame['PATNA'])
	plt.subplot(515)
	plt.plot(newFrame['BHUBANESHWAR'])
	plt.show()


#plt.plot(retail['DELHI'])
#plt.plot(retail['LUCKNOW'])	#somewhat flat
#plt.plot(retail['PATNA'])	#somewhat flat and follow
#plt.show()
#plt.plot(retail['MUMBAI'])	#seems to follow
#plt.plot(retail['BHUBANESHWAR'])	#seems to follow
#plt.show()

#no stats common ground found
'''
print("----------MEAN------------")
print(newFrame['DELHI'].mean())
print(newFrame['LUCKNOW'].mean())
print(newFrame['MUMBAI'].mean())
print(newFrame['PATNA'].mean())
print(newFrame['BHUBANESHWAR'].mean())
print("----------VARIANCE------------")
print(newFrame['DELHI'].var())
print(newFrame['LUCKNOW'].var())
print(newFrame['MUMBAI'].var())
print(newFrame['PATNA'].var())
print(newFrame['BHUBANESHWAR'].var())
print("-----------STD-----------")
print(newFrame['DELHI'].std())
print(newFrame['LUCKNOW'].std())
print(newFrame['MUMBAI'].std())
print(newFrame['PATNA'].std())
print(newFrame['BHUBANESHWAR'].std())
print("----------------------")
'''	


#plot some of the mandis len(selectedAnom)
for i in range(0, 1):
	startIndex = (datetime.datetime.strptime(selectedAnom['start'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	endIndex = (datetime.datetime.strptime(selectedAnom['end'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	newFrame1 = retail.ix[startIndex:endIndex]
	newFrame = arrival.ix[startIndex:endIndex]
	plt.figure(1)
	plt.subplot(511)
	plt.plot(newFrame1['DELHI'])
	plt.subplot(512)
	plt.plot(newFrame[0])
	plt.subplot(513)
	plt.plot(newFrame[1])
	plt.subplot(514)
	plt.plot(newFrame[2])
	plt.subplot(515)
	plt.plot(newFrame[3])
	plt.show()
	plt.figure(2)
	plt.subplot(511)
	plt.plot(newFrame1['DELHI'])
	plt.subplot(512)
	plt.plot(newFrame[4])
	plt.subplot(513)
	plt.plot(newFrame[5])
	plt.subplot(514)
	plt.plot(newFrame[6])
	plt.subplot(515)
	plt.plot(newFrame[7])
	plt.show()
	plt.figure(3)
	plt.subplot(411)
	plt.plot(newFrame1['DELHI'])
	plt.subplot(412)
	plt.plot(newFrame[8])
	plt.subplot(413)
	plt.plot(newFrame[9])
	plt.subplot(414)
	plt.plot(newFrame[10])
	plt.show()

newFrame = arrival
plt.plot(newFrame[5])
plt.plot(newFrame[6])
plt.plot(newFrame[7])
plt.plot(newFrame[8])
plt.plot(newFrame[9])
plt.show()

labels = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
d = [i*365 for i in range(1,10)]


x = 311
#plt.title("All Hoarding Instance")
x = 0
plt.plot(retail['DELHI'])#, label='DELHI')
plt.plot(retail['LUCKNOW'])#, label='LUCKNOW')
plt.plot(retail['MUMBAI'])#, label='MUMBAI')
plt.plot(retail['PATNA'])#, label='PATNA')
plt.plot(retail['BHUBANESHWAR'])#, label='BHUBANESHWAR')

index = [1,6,17,19,14]
selectedAnom = anom.ix[index].reset_index()
for i in range(0, len(selectedAnom)):
	startIndex = (datetime.datetime.strptime(selectedAnom['start'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	endIndex = (datetime.datetime.strptime(selectedAnom['end'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	plt.plot([startIndex, startIndex], [0,8000], 'r', label='Seasonal')
	plt.plot([endIndex, endIndex], [0,8000], 'r')

index = [ 0, 4, 16]
selectedAnom = anom.ix[index].reset_index()
for i in range(0, len(selectedAnom)):
	startIndex = (datetime.datetime.strptime(selectedAnom['start'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	endIndex = (datetime.datetime.strptime(selectedAnom['end'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	plt.plot([startIndex, startIndex], [0,8000], 'g', label='Others')
	plt.plot([endIndex, endIndex], [0,8000], 'g')

index = [8,9,12,20]
selectedAnom = anom.ix[index].reset_index()
for i in range(0, len(selectedAnom)):
	startIndex = (datetime.datetime.strptime(selectedAnom['start'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	endIndex = (datetime.datetime.strptime(selectedAnom['end'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	#newFrame = retail.ix[0:3460]
	#plt.figure(1)
	#plt.subplot(x)
	#y = "Hoarding Anom " + str(x)
	x = x + 1
	plt.plot([startIndex, startIndex], [0,8000], 'c', label='Hoarding')
	plt.plot([endIndex, endIndex], [0,8000], 'c')
	plt.xlabel("Days")
	plt.ylabel("Prices")
	#plt.title(y)
	#plt.xticks(d, labels, rotation='vertical')
	#print(endIndex-startIndex)
plt.xticks(d, labels, rotation='vertical')
plt.legend(loc='upper right')
plt.show()


/(newFrame['DELHI'].mean())

x = 0
for i in range(0, len(selectedAnom)):
	startIndex = (datetime.datetime.strptime(selectedAnom['start'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	endIndex = (datetime.datetime.strptime(selectedAnom['end'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	newFrame = retail.ix[startIndex:endIndex]
	#plt.figure(1)
	#plt.subplot(x)
	y = "Hoarding Anom " + str(x)
	plt.plot(newFrame['DELHI']/(newFrame['DELHI'].mean()), label='DELHI')
	plt.plot(newFrame['LUCKNOW']/(newFrame['LUCKNOW'].mean()), label='LUCKNOW')
	plt.plot(newFrame['MUMBAI']/(newFrame['MUMBAI'].mean()), label='MUMBAI')
	plt.plot(newFrame['PATNA']/(newFrame['PATNA'].mean()), label='PATNA')
	plt.plot(newFrame['BHUBANESHWAR']/(newFrame['BHUBANESHWAR'].mean()), label='BHUBANESHWAR')
	x = x + 1
	#plt.plot([startIndex, startIndex], [0,8000])
	#plt.plot([endIndex, endIndex], [0,8000])
	plt.xlabel("Days")
	plt.ylabel("Prices")
	plt.title(y)
	#plt.xticks(d, labels, rotation='vertical')
	print(endIndex-startIndex)
	plt.legend(loc='upper right')
	plt.show()


#index = [8,9,12,20]
#index = [1,6,17,19,14]
index = [ 0, 4, 16]
x = 0
selectedAnom = anom.ix[index].reset_index()
for i in range(0, len(selectedAnom)):
	startIndex = (datetime.datetime.strptime(selectedAnom['start'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	endIndex = (datetime.datetime.strptime(selectedAnom['end'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	newFrame1 = retail.ix[startIndex:endIndex]
	newFrame = ws.ix[startIndex:endIndex]
	y = "Hoarding Anom " + str(x)
	plt.figure(1)
	plt.plot(newFrame1['DELHI'], label = "DELHI")
	plt.plot(newFrame[0], label = 'Mandi1')
	plt.plot(newFrame[1], label = 'Mandi2')
	plt.plot(newFrame[2], label = 'Mandi3')
	plt.plot(newFrame[3], label = 'Mandi4')
	plt.plot(newFrame[4], label = 'Mandi5')
	plt.plot(newFrame[5], label = 'Mandi6')
	plt.plot(newFrame[6], label = 'Mandi7')
	plt.plot(newFrame[7], label = 'Mandi8')
	plt.plot(newFrame[8], label = 'Mandi9')
	plt.plot(newFrame[9], label = 'Mandi10')
	plt.plot(newFrame[10], label = 'Mandi11')
	plt.xlabel("Days")
	plt.ylabel("Prices")
	plt.title(y)
	plt.legend(loc='upper right')
	plt.show()
	x = x + 1



import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from scipy import signal

from sklearn.decomposition import FastICA, PCA
retail = pd.read_csv("processed_retail.csv")
X = retail.ix[:,1:6]

ica = FastICA(n_components=2)
S_ = ica.fit_transform(X)
A_ = ica.mixing_

#for i in range(0, len(A_)):
plt.plot(S_.T[i]*A_[2][i] + ica.mean_[2])
plt.plot(X["DELHI"], 'r')
plt.show()

pic1 = ic1
pic2 = ic2
pa_ = A_
ps_ = S_


ic1 = S_.T[0]
ic2 = S_.T[1]
ic3 = S_.T[2]
ic4 = S_.T[3]
ic5 = S_.T[4]

plt.plot(ic1)
plt.show()
plt.plot(ic2)
plt.plot(ic3)
#plt.plot(ic4)
#plt.plot(ic5)

rc11 = ic1*A_[4][0]
rc12 = ic2*A_[4][1]
rc11
rc12
ica.mean_[4]

0:= Patna
1:= Mumbai
2:= Delhi
3:= BHUBANESHWAR
4:=LUCKNOW
'''
S_ = S_*100000
A_ = A_/100000

df = pd.DataFrame()
df[0] = S_.T[0]
df[1] = S_.T[1]
df[2] = S_.T[2]
df[3] = S_.T[3]
df[4] = S_.T[4]

ica = FastICA(n_components=2)
s_ = ica.fit_transform(X)
a_ = ica.mixing_
'''

from statsmodels.tsa.seasonal import seasonal_decompose
series = retail["DELHI"]
result = seasonal_decompose(series, model='additive')
print(result.trend)
print(result.seasonal)
print(result.resid)
print(result.observed)

from random import randrange
from pandas import Series
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose
series = [i+randrange(10) for i in range(1,100)]
result = seasonal_decompose(series, model='additive', freq=1)
result.plot()
pyplot.show()

t = []
for i in range(0,3461):
	t.ix[i] = (retail["DELHI"].ix[i] - trend.ix[i])