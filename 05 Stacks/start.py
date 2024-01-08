''' Stacks '''

# Stacks werden durch Listen btw. Arrays repräsentiert
# Ein Stack bestitzt eine abstrakte Datenstruktur
# Es gilt hier das LIFO-Prinzip (Last-In-First-Out)

# Initialisierung eines leeren Stapels
stack = []

# Push/Append: Hinzufügen eines Elements
stack.append(22)
stack.append(0)
stack.append(1)
stack.append(232)

# Pop: Auslesen und Entfernen des obersten Elements
element = stack.pop()

# Peek oder Top: Auslesen des obersten Elements (ohne Entfernen)
element = stack[-1]

# isEmpty: Prüfen, ob der Stack leer ist
leer = len(stack) == 0

print(stack)