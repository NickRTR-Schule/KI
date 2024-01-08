# UPN Taschenrechner

stack = []
ergebnis = 0

# Eingabe einlesen
while(True):
    eingabe = input("Eingabe: ")
    if eingabe == "q":
        break
    if eingabe == "+":
        stack.append(stack.pop() + stack.pop())
    elif eingabe == "*":
        stack.append(stack.pop() * stack.pop())
    elif eingabe == "-":
        zahl1 = stack.pop()
        zahl2 = stack.pop()
        stack.append(zahl2 - zahl1)
    elif eingabe == "/":
        zahl1 = stack.pop()
        zahl2 = stack.pop()
        stack.append(zahl2 / zahl1)
    else:
        stack.append(int(eingabe))  

print("Ergebnis: ", stack.pop())
