import numpy as np # Mit der Numpy-Bibliothek ist die Verarbeitung deutlich leistungsstärker
import func

'''Listen'''
# Eine Liste ist eine geordnete Datenstruktur aus Elementen
# Innerhalb der Programmierung werden Listen oft durch Arrays repräsentiert

# Initialisierung mit eckigen Klammerm
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
npListe = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Es gibt veränderbare (mutable) und unveränderbare (immutable) Listen
tupelListe = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) # Tubel entspricht immutable

# Listen können beliebige Datentypen enthalten
liste = [1, 2.1, True, "Hallo"]
npListe = np.array([1, 2.1, True, "Hallo"])

# Zugriff auf ein Element in der Liste
print(liste[2]) 
print(npListe[2])
print(liste[-1]) # Zugriff auf das letzte Element

# Überprüfung der Anwesenheit eines ELements mit dem in-Operator
if 1 in liste: print("1 ist drin")
if 1 in npListe: print("1 ist drin")

# Länge (Dimension) einer Liste abrufen
length1 = len(liste)
length2 = len(npListe)
length3 = np.size(npListe)

print(length1, length2, length3)

# Slicing: Zugriff auf Teile der Liste
print(liste[2:6])
print(npListe[2:6])

# Verwendung von Schleifen
# for i in liste:
#     print(i, end=" ") # End überschreibt new line

# for i in range(np.size(npListe)):
#     print(npListe[i], end=" ")

# Verschachtelung von Listen -> Mehrdimensionale Arrays
    
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

vListe = [list1, list2, list3]
npVListe = np.array([list1, list2, list3])

# Zugriff auf ein Element in der mehrdimensionalen Liste
print(vListe[0][0]) 

# -------------------- Aufgaben --------------------

print(func.aufgabe1())
print("-------------------- Aufgabe 2 --------------------")
spielbrett = func.aufgabe2()
print(spielbrett)
print("-------------------- Aufgabe 2c -------------------")
func.aufgabe2c(spielbrett)
