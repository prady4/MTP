ws = pd.read_csv("WS.csv", header=None)
a = ws[ws[1] == 182]
b = ws[ws[1] == 174]
c = ws[ws[1] == 194]

f = c
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
c = f

