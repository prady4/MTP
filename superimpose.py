import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

#pre-process
e = pd.read_csv("centres.csv")

d = pd.read_csv("ii.csv", header=None)

e = e.set_index("cid")
e = e.ix[pairs]

plt.plot(d[0], d[1])
plt.plot(e["long"], e["lat"], 'o', color='r')

