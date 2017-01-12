import whitening as wt

#factor right now 0.1
#centreID 0,1,2,3,4
def get_anom(factor, centreID):
	(resid, s_, a_) = wt.ICA(wt.centres2, 2, 3461)
	window = wt.CreateWindow(wt.centres2, factor, 3461)
	anom = wt.ExtractAnomalies(resid, window, centreID, 3461)
	s = []
	e = []
	start = anom[0]
	end = anom[0]
	for i in range(1,len(anom)):
		if (anom[i].date() - anom[i-1].date()).days < 7:
			end = anom[i]
		elif (anom[i].date() - anom[i-1].date()).days >= 7:
			if (start.date() - end.date()).days != 0:
				s.append(start)
				e.append(end)
				start = anom[i]
				end = anom[i]
	for i in s:
		print(i.date())
	print("########")
	for i in e:
		print(i.date())
	return anom


def windows():
	s = []
	e = []
	start = anom[0]
	for i in range(1,len(anom)):
		if (anom[i].date() - anom[i-1].date()).days < 7:
			end = anom[i]
		elif (anom[i].date() - anom[i-1].date()).days >= 7:
			if (start.date() - end.date()).days != 0:
				s.append(start)
				e.append(end)
				start = anom[i]
				end = anom[i]
	for i in s:
		print(i.date())
	print("#######")
	for i in e:
		print(i.date())

df['slope'] = df.apply(lambda x: 0 if ((b.ix[x['level_0']+7]['price'] - b.ix[x['level_0']]["price"])*x['price'] == 0) else (((a.ix[x['level_0']+7]['price'] - x['price'])*b.ix[x['level_0']]["price"])/((b.ix[x['level_0']+7]['price'] - b.ix[x['level_0']]["price"])*x['price'])), axis=1)