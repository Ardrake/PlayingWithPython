'''Write a program to draw a Sprite where the number of legs is provided by the user.'''

import turtle

Sprite = turtle.Turtle

numLegs = 5
x = 0
y = -100
Sprite.setpos(x,y)


for i in range(numLegs):
    Sprite.forward(10)

