#!/usr/bin/env python3
# This program is for
# Author: MYGNU

# Please feel free to copy, distribute and modify till your heart is content

import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

sq = turtle.Turtle()

def crsqr(t,num):
    """creates squares of 20 units, takes turtle object and number of squares max 10
    """
    sz = 20
        
    while sz <= num:
        
        t.forward(sz)
        t.right(90)
        t.forward(sz)
        t.right(90)
        t.forward(sz)
        t.right(90)
        t.forward(sz)
        t.up()
        t.forward(10)
        t.right(90)
        t.backward(10)
        t.down()
        sz += 20

sq.pensize(4)
sq.color('hotpink')
crsqr(sq,300)

wn.exitonclick()

