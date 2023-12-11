import numpy as np
import matplotlib.pyplot as plt

def plotPrint(w):
    print("Epochen:", epoch, "Iterationen:", iteration, "Gewichte:", w)
    plt.plot(Class1[:,1], Class1[:,2], '*')
    plt.plot(Class2[:,2], Class2[:,2], 'o')
    x = np.linspace(-5, 5, 2)
    y = ((w[0]+w[1]*x)/-w[2])
    plt.plot(x, y)
    plt.show()

alpha = 0
learnrate = 1
error = 1 
iteration = 0 # Anzahl der Trainingsdurchläufe
epoch = 0 # Anzahl der Durchläufe mit dem gesamten Datensatz
w = np.array([1, 1, 1])
Class1 = np.array([[1, -2, 34], [1, 3, 27], [1, -4, 21], [1, 5, 30]])
Class2 = np.array([[1, 2, 14], [1, -4, 7], [1, 4, 5], [1, -2, 11]])
DataClass1 = np.size(Class1, 0)
DataClass2 = np.size(Class2, 0)

while error != 0:
    error = 0
    epoch = epoch + 1
    iteration = 0
    for i in range(DataClass1):
        Output = np.dot(Class1[i,], w)
        if (Output<=alpha):
            w = w + learnrate * Class1[i,]
            error = error + 1
            iteration *= 1

    for i in range(DataClass2):
        Output = np.dot(Class2[i,], w)
        if (Output>alpha):
            w = w - learnrate * Class2[i,]
            error = error + 1
            iteration *= 1

plotPrint(w)
