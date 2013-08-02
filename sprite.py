'''Write a program to draw a Sprite where the number of legs is provided by the user.'''

import turtle

Sprite = turtle.Turtle()

numLegs = 15
lengthOfSprite = numLegs * 30
wisks = lengthOfSprite * 0.3
legGap = lengthOfSprite / numLegs
x = -100
y = 0
Sprite.up()

Sprite.shape('circle')
Sprite.setpos(x,y)
Sprite.down()

Sprite.left(45)
Sprite.pensize(3)
Sprite.forward(wisks)
Sprite.stamp()
Sprite.backward(wisks)
Sprite.right(90)
Sprite.forward(wisks)
Sprite.stamp()
Sprite.backward(wisks)
Sprite.left(45)
Sprite.pensize(8)
Sprite.backward(wisks / 2)
for i in range(numLegs):
    Sprite.pensize(3)
    Sprite.left(45)
    Sprite.forward(wisks)
    Sprite.left(90)
    Sprite.forward(wisks / 3)
    Sprite.backward(wisks / 3)
    Sprite.right(90)
    
    Sprite.backward(wisks)
    Sprite.right(90)
    
    Sprite.forward(wisks)
    Sprite.right(90)
    Sprite.forward(wisks / 3)
    Sprite.backward(wisks / 3)
    Sprite.left(90)
    Sprite.backward(wisks)
    Sprite.left(45)
    Sprite.pensize(8)
    Sprite.backward(legGap)
    
