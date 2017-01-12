import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

anom = pd.read_csv("anom1.tsv", sep='\t')
retail = pd.read_csv("processed_retail.csv")
index = [2,4,5,13,17]
selectedAnom = anom.ix[index].reset_index()

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

