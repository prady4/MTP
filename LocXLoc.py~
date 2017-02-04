import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

anom = pd.read_csv("anom.csv", header=None)
anom = np.array(anom.values.tolist()).T
anom = [[x for x in anom[i] if str(x) != 'nan'] for i in range(0, len(anom))]
anom = np.array(anom)

#matrix = [[[0 for p in range(0,len(anom[2*j]))] for i in range(0,5)] for j in range(0,5)]

def create_vector(list1, list2):
	vec = [0]*3461
	for x in range(0, len(list1)):
		start = list1[x]
		end = list2[x]
		startIndex = (datetime.datetime.strptime(start, '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
		endIndex = (datetime.datetime.strptime(end, '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
		for i in range(startIndex, endIndex):
			vec[i] = 1
	return np.array(vec)

for i in range(0,5):
	m = i*2
	vec1 = create_vector(anom[m], anom[m+1])
	vec1 = vec1*3
	for j in range(0,5):
		if i != j:
			k = j*2
			vec2 = create_vector(anom[k], anom[k+1])
			ans = vec1 - vec2
			for x in range(0, len(anom[m])):
				start = anom[m][x]
				end = anom[m+1][x]
				startIndex = (datetime.datetime.strptime(start, '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
				endIndex = (datetime.datetime.strptime(end, '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
				y = ans[startIndex:endIndex+1]
				matrix[i][j][x] = y.tolist().count(2)
		else:
			for x in range(0, len(anom[m])):
				start = anom[m][x]
				end = anom[m+1][x]
				startIndex = (datetime.datetime.strptime(start, '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
				endIndex = (datetime.datetime.strptime(end, '%d/%m/%Y') - datetime.datetime.strptime('01Jan2006', '%d%b%Y')).days
				matrix[i][j][x] = endIndex - startIndex + 1


matrix = [[[13, 45, 27, 16, 25, 13, 15, 42, 2, 5, 20, 21, 10, 22, 80, 4, 71, 84], [4, 25, 20, 15, 24, 4, 8, 16, 1, 1, 18, 20, 4, 17, 78, 0, 70, 83], [12, 44, 22, 8, 24, 1, 0, 18, 0, 0, 19, 4, 0, 18, 33, 0, 63, 55], [4, 23, 20, 6, 11, 1, 0, 0, 0, 1, 19, 7, 0, 18, 76, 0, 51, 28], [12, 44, 26, 9, 24, 12, 14, 41, 0, 4, 13, 20, 9, 21, 46, 2, 70, 83]], [[4, 24, 1, 20, 43, 8, 11, 5, 0, 0, 1, 1, 18, 0, 20, 4, 17, 78, 70, 83], [6, 34, 2, 21, 82, 9, 12, 7, 7, 22, 7, 2, 22, 2, 33, 5, 18, 79, 71, 138], [5, 33, 1, 18, 45, 0, 11, 5, 0, 0, 0, 0, 21, 0, 4, 0, 14, 33, 63, 81], [5, 31, 1, 18, 42, 0, 0, 0, 0, 0, 0, 1, 19, 1, 18, 0, 14, 76, 51, 28], [5, 33, 1, 20, 69, 8, 11, 6, 0, 0, 0, 1, 12, 0, 23, 4, 17, 45, 70, 86]], [[12, 44, 22, 32, 1, 0, 12, 6, 0, 0, 0, 19, 4, 18, 32, 1, 63, 55], [5, 34, 18, 44, 1, 0, 11, 5, 0, 0, 0, 21, 4, 14, 32, 1, 63, 81], [22, 58, 24, 45, 2, 6, 16, 7, 5, 10, 12, 24, 5, 23, 33, 2, 64, 82], [5, 35, 20, 29, 0, 0, 0, 0, 0, 6, 0, 20, 4, 18, 32, 1, 51, 3], [21, 56, 23, 44, 1, 5, 12, 6, 0, 9, 0, 13, 4, 18, 32, 0, 63, 55]], [[4, 22, 1, 20, 6, 11, 1, 0, 0, 0, 1, 26, 18, 76, 51, 28], [5, 31, 1, 18, 17, 25, 0, 0, 0, 0, 1, 38, 14, 76, 51, 28], [5, 34, 1, 20, 17, 12, 0, 0, 0, 6, 0, 24, 18, 33, 51, 3], [6, 35, 4, 21, 18, 26, 2, 14, 8, 7, 2, 192, 19, 77, 52, 29], [5, 34, 3, 20, 17, 25, 1, 0, 0, 6, 1, 23, 18, 43, 51, 28]], [[12, 70, 59, 41, 0, 0, 4, 13, 50, 37, 9, 72, 83], [5, 54, 77, 17, 0, 0, 1, 12, 44, 36, 9, 70, 86], [21, 79, 50, 18, 9, 0, 0, 13, 22, 32, 0, 63, 55], [5, 57, 43, 0, 6, 0, 1, 14, 27, 34, 9, 51, 28], [23, 105, 125, 43, 11, 2, 5, 15, 119, 39, 10, 114, 87]]]
#3d Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
i = 0
for c, z in zip(['r', 'g', 'b', 'y', 'c'], [40, 30, 20, 10, 0]):
	xs = np.arange(len(matrix[1][0]))	#1 for delhi
	ys = matrix[1][i]	#index of other centres
	cs = [c] * len(xs)
	cs[0] = 'c'
	ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)
	i = i + 1

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
