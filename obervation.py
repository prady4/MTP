import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#read CSVs
mandi = pd.read_csv("subset_mandi.csv")
centres = pd.read_csv("subset_centres.csv")
data = pd.read_csv("subset_retail.csv")
ws = pd.read_csv("subset_ws.csv")



#intermediate_results
mandi_id = [11, 35, 31, 182, 174, 194, 281, 404, 351, 312, 165, 70, 293, 164, 447, 407, 166, 345, 337, 577, 545, 323, 405, 284, 324, 584, 285, 278, 288, 325, 279, 376]
cid = [3, 10, 16, 37, 40, 50]
mandi_s = [0, 3, 1, 0, 3, 0, 11, 0, 0, 1, 1, 3, 9, 2, 3, 0, 0, 0, 0]
centres_s = [1, 3, 7, 9, 10, 12, 16, 23, 27, 31, 32, 37, 40, 44, 50, 54, 61, 62, 68]
mid = [[], [11, 35, 31], [109], [], [182, 174, 194], [], [281, 404, 351, 312, 165, 70, 293, 164, 447, 407, 166], [], [], [394], [89], [345, 337, 577], [545, 323, 405, 284, 324, 584, 285, 278, 288], [156, 427], [325, 279, 376], [], [], [], []]


ws['date'] =  pd.to_datetime(ws['date'], format='%Y-%m-%d')
ws.set_index('date', inplace=True)
idx = pd.date_range('2006-01-01', '2015-06-23')
m = m.reindex(idx, fill_value=0)
m.reset_index(level=0, inplace=True)


'''
data['date'] =  pd.to_datetime(data['date'], format='%Y-%m-%d')
data['day'] = data['date'].dt.dayofweek
data = data[(data["day"] != 6) and (data["day"] != 5)]

ws['date'] =  pd.to_datetime(ws['date'], format='%Y-%m-%d')
ws['day'] = ws['date'].dt.dayofweek
ws = ws[(ws["day"] != 6) and (ws["day"] != 5)]

#No weekends, Threshold 80%
centres_s = [1, 3, 7, 9, 10, 12, 16, 23, 27, 31, 32, 37, 40, 44, 50, 54, 61, 62, 68]
mandi_s = [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0]
mid = [[], [], [], [], [], [], [312, 164, 166], [], [], [], [], [], [278, 288], [], [279], [], [], [], []]

#No weekends, Threshold 60%
centres_s = [1, 3, 4, 5, 7, 9, 10, 11, 12, 15, 16, 23, 27, 31, 32, 37, 40, 41, 44, 50, 54, 56, 61, 62, 64, 68]
mandi_s = [0, 3, 0, 3, 1, 0, 2, 10, 0, 2, 12, 0, 0, 1, 1, 3, 10, 20, 4, 2, 0, 4, 0, 1, 0, 0]
mid = [[], [11, 35, 31], [], [261, 259, 223], [109], [], [182, 194], [232, 241, 204, 210, 256, 507, 726, 200, 206, 234], [], [318, 459], [281, 404, 351, 312, 165, 70, 293, 164, 447, 758, 407, 166], [], [], [394], [89], [345, 337, 577], [295, 545, 323, 405, 284, 324, 584, 285, 278, 288], [225, 215, 203, 219, 202, 227, 198, 205, 222, 389, 246, 434, 231, 492, 213, 218, 238, 254, 245, 237], [163, 427, 146, 148], [325, 279], [], [99, 106, 93, 342], [], [86], [], []]


'''

for i in mandi_id:
	a = ws[ws["mid"]==i]
	a["arrival"].max()
#plots

