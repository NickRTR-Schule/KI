import numpy as np

from func import *

weekend = np.genfromtxt("ape.csv", delimiter=",", dtype=str)

print("Gesamt-Gini:", round(giniGesamt(weekend), 2))
print("Bester Wurzelknoten des Entscheidungsbaumes:", bestGini(weekend))