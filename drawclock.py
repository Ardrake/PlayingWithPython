'''this program draws a five corner star'''
#  ntoehunt

import turtle
wn = turtle.Screen()
wn.bgcolor('lightblue')
clock = turtle.Turtle()
clock.pencolor('blue')
clock.pensize(5)
clock.fillcolor('red')
clock.shape('turtle')
clock.up()
clock.stamp()

for i in range(12):
    
    clock.right(30)
    clock.forward(100)
    clock.down()
    clock.forward(20)
    clock.up()
    clock.forward(30)
    clock.stamp()
    clock.backward(150)

