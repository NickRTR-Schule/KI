import numpy as np

from func import *

weekend = np.genfromtxt("weekend.csv", delimiter=",", dtype=str)

print("Bester Wurzelknoten des Entscheidungsbaumes:", bestGini(weekend))