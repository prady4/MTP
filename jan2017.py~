import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

f.columns = ["date", "mid", "arrival", "origin", "var", "min", "max", "price"]
f = f[f["date"] >= "2006-01-01"]
f = f[f["date"] <= "2015-06-23"]
f = f.sort(["date"], ascending = True)
f = f.drop_duplicates(cols='date', take_last=True)
f['date'] =  pd.to_datetime(f['date'], format='%Y-%m-%d')
f.set_index('date', inplace=True)
idx = pd.date_range('2006-01-01', '2015-06-23')
f = f.reindex(idx)
f.reset_index(level=0, inplace=True)
f = f.interpolate(method='pchip')

labels = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
d = [i*365 for i in range(1,10)]

#retail data plot
data = pd.read_csv("retail_data.csv")
anomalies = pd.read_csv('anom0.tsv', sep='\t')
for i in range(0, len(anomalies['start'])):
	#plot data
	plt.plot(a["price"], color = 'b', label="Mandi1")
	plt.plot(b["price"], color = 'g', label="Mandi2")
	plt.plot(c["price"], color = 'r', label="Mandi3")
	#centre
	plt.plot(data["10"], color = 'c', label="Centre")
	#plot anom
	diff = (datetime.datetime.strptime(anomalies['start'][i], '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
	plt.plot([diff, diff], [0, 7000])
	diff = diff + (datetime.datetime.strptime(anomalies['end'][i], '%d/%m/%Y') - datetime.datetime.strptime(anomalies['start'][i], '%d/%m/%Y')).days
	plt.plot([diff, diff], [0, 7000])
	plt.xticks(d, labels, rotation='vertical')
	plt.legend(loc='upper right')
	plt.show()







