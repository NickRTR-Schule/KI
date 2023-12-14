import numpy as np
import matplotlib.pyplot as plt

def plotten():
    plt.scatter(data, data*0, c=label) # Daten
    plt.scatter(center, center*0, c='red', s=200) # Zentren
    plt.title('1D K-MEANS Clustering')
    plt.show()

# Generierung von Beispieldaten
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
dataLen = np.size(data)

# Generierung von Initialzentren
center = np.array([10, 20])

# Zuordnung der Datenpunkte zu den Zentren
label = data * 0

plotten()

for i in range(3):
    sum1 = 0
    sum2 = 0
    count1 = 0
    count2 = 0

    diff1 = np.abs(data - center[0])
    diff2 = np.abs(data - center[1])

    for j in range(dataLen):
        if diff1[j] < diff2[j]:
            label[j] = 1
            sum1 += data[j]
            count1 += 1
        else:
            label[j] = 2
            sum2 += data[j]
            count2 += 1

    center[0] = sum1 / count1
    center[1] = sum2 / count2

    plotten()