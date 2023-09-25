import numpy as np

from func import gini

weekend = np.genfromtxt("weekend.csv", delimiter=",", dtype=str)

print(gini(weekend))
