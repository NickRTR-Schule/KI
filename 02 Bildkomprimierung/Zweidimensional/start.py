import numpy as np
import matplotlib.pyplot as plt
import math

def plotten():
    plt.title('1D K-MEANS Clustering')
    plt.plot(data[:,0],data[:,1],'.')
    plt.plot(center[:,0],center[:,1],'o')
    plt.show()

# Generierung von Beispieldaten
points = 100
posData1 = 10
posData2 = 50
spread = 20
dimension = 2
data = np.random.normal(posData1,spread,(points,dimension))
dataLen = np.size(data)

# Generierung von Initialzentren
center = np.array([[-20, 20], [20, 20]])

# Zuordnung der Datenpunkte zu den Zentren
label = np.zeros(99)

#plotten()

for i in range(3):
    sum1 = [0, 0]
    sum2 = [0, 0]
    count1 = 0
    count2 = 0

    diff1 = []
    diff2 = []
    for j in range(99):
        print(j)
        diff1.append(math.sqrt((data[j][0]-center[0][0])**2 + (data[j][1]-center[0][1])**2))
        diff2.append(math.sqrt((data[j][0]-center[1][0])**2 + (data[j][1]-center[1][1])**2))
    
    print(diff1)

    for z in range(99):
        if diff1[z] < diff2[z]:
            label[z] = 1
            sum1[0] += data[z][0]
            sum1[1] += data[z][1]
            count1 += 1
        else:
            label[z] = 2
            sum2[0] += data[z][0]
            sum2[1] += data[z][1]
            count2 += 1

    center[0][0] = sum1[0] / count1
    center[0][1] = sum1[1] / count1
    center[1][0] = sum2[0] / count2
    center[1][1] = sum2[1] / count2

    plotten()