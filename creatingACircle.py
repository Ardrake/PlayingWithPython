import turtle
from math import pi

wn = turtle.Screen()
tcircle = turtle.Turtle()


def mycircle(t,r):
    '''Creates circle by taking two arguments "turtle object" and "diameter".'''

    cirf = 2 * r * pi # calculating the circumference of the circle
    fwd = cirf/100    # to forward the turtle 100 times on the circumference 
    for i in range(100):
        t.forward(fwd)
        t.right(3.6) # turn right 100 times to complete the circle 360 / 100

def cofc(t,r):
    '''Creates circle of circle by taking two arguments
    "turtle object" and "diameter".'''
    coc_cirf = 2 * r * pi  # calculating the circumference of the circle
    fwd = coc_cirf / 50    # forward by the diameter of small circles
    r_of_small_c = fwd / 2 # radious of small circles
    t.speed(0)
    for i in range(100):
        mycircle(t,r_of_small_c)     
        t.up()
        t.right(3.6)
        t.forward(fwd)
        t.down()

cofc(tcircle, 100)

wn.exitonclick()
