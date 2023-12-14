import numpy as np
import random

def aufgabe1():
    array = np.zeros(100)
    for i in range(100):
        array[i] = random.randint(0, 100)

    over90 = np.array([i for i in array if i > 90])
    return over90

def aufgabe2():
    spielbrett = np.zeros((5, 5))

    # Create 5 random ships
    counter = 0
    while (counter < 5):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if spielbrett[x][y] != 1:
            spielbrett[x][y] = 1
            counter += 1

    # Shot until all ships are destroyed
    destroyCounter = 0
    while (destroyCounter < 5):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if spielbrett[x][y] == 1:
            spielbrett[x][y] = 2
            destroyCounter += 1
            print("Treffer")
        else:
            print("Daneben")
    print("Alle Schiffe versenkt")
    return spielbrett

def aufgabe2c(spielbrett):
    for _ in range(5):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if spielbrett[x][y] == 2:
            spielbrett[x][y] = 3
            print("Treffer")
        else:
            print("Daneben")
