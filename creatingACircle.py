import turtle
from math import pi

wn = turtle.Screen()
tcircle = turtle.Turtle()


def mycircle(t,r):
    '''Creates circle by taking two arguments "turtle object" and "diameter".'''

    cirf = 2 * r * pi
    fwd = cirf/100
    for i in range(100):
        t.forward(fwd)
        t.right(3.6)

def cofc(t,r):
    '''Creates circle of circle by taking two arguments
    "turtle object" and "diameter".'''
    coc_cirf = 2 * r * pi
    fwd = coc_cirf / 50
    r_of_small_c = fwd / 2
    t.speed(10)
    for i in range(100):
        mycircle(t,r_of_small_c)     
        t.up()
        
        t.right(3.6)
        t.forward(fwd)
        t.down()

cofc(tcircle, 100)

wn.exitonclick()
