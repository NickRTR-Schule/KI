import turtle

def kloetze(hoehe):
    if (hoehe == 1):
        return 1
    else:
        return hoehe + kloetze(hoehe - 1)
    
def draw(w,l,i):
    if (i<8):
        turtle.forward(l)
        turtle.left(w)
        turtle.forward(l)
        turtle.right(w)
        draw(w,l*0.9,i+1)
        