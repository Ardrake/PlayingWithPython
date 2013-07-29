'''Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
    An equilateral triangle
    A square
    A hexagon (six sides)
    An octagon (eight sides)'''



import turtle

tr = turtle.Turtle()

for i in (1,2,3):
	tr.left(120)
	tr.forward(80)

tr.up()
tr.goto(-105,0)    
tr.down()

for i in range(4):
    tr.left(90)
    tr.forward(80)

tr.up()
tr.goto(-105,-120)    
tr.down()

for i in range(6):
    tr.left(60)
    tr.forward(40)

tr.up()
tr.goto(20,-120)    
tr.down()

for i in range(8):
    tr.left(45)
    tr.forward(30)

