#!/usr/bin/env python3
# This program is for
# Author: MYGNU

# Please feel free to copy, distribute and modify till your heart is content

import turtle

wn = turtle.Screen()

sq = turtle.Turtle()

def crsqr(t,num):
    """creates squares of 20 units, takes turtle object and number of squares max 10
    """
    sz = 20
    for i in range(num):
        t.left(90)
        t.forward(sz)
        t.right(90)
        t.forward(sz)
        t.right(90)
        t.forward(sz)
        t.right(90)
        t.forward(sz)
        t.right(180)
        t.up()
        t.forward(sz *2)
        t.down()

crsqr(sq,5)

wn.exitonclick()