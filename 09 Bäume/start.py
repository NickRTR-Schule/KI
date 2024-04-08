class Node: 
    def __init__(self, value): 
        self.l = None
        self.r = None
        self.kopf = value

    def istLinksLeer(self):
        if (self.l is None):
            return True
        else:
            return False
        
    def istRechtsLeer(self):
        if (self.l is None):
            return True
        else:
            return False
        
def printTree(wurzel):
    if (wurzel != None):
        #print(wurzel.kopf) # Pre-Order
        printTree(wurzel.l)
        #print(wurzel.kopf) # In-Order
        printTree(wurzel.r)
        print(wurzel.kopf) # Post-Order
        
# Baum erzeugen
wurzel = Node(1)
wurzel.l = Node(2)
wurzel.r = Node(3)
wurzel.l.l = Node(4)
wurzel.l.r = Node(5)
wurzel.l.r.l = Node(6)

# Kind Abfrage
print('Wurzel->links->links leer?', wurzel.l.istLinksLeer())
print('Wurzel->rechts->rechts leer?', wurzel.r.istRechtsLeer())

# Baum vollständig ausdrucken 
printTree(wurzel)