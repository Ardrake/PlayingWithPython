import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()

fline = turtle.Turtle()
fline.color('green')
fline.up()
fline.setpos(100, 50)
fline.down()
fline.right(90)
fline.forward(100)




lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-200,20)
lance.goto(-200,-20)
ran1 = -100
ran2 = -100
# your code goes here

for i in range(1,50,1):
    prevran1 = ran1
    prevran2 = ran2
    ran1 = random.randint(1,10)
    ran2 = random.randint(1,10)
    #andy.goto(prevran1,ran1)
    #lance.goto(prevran2,ran2)
    andy.forward(ran1)
    lance.forward(ran2)
wn.exitonclick()

