'''A drunk pirate makes a random turn and then takes 100 steps forward, 
makes another random turn, takes another 100 steps, turns another random amount, etc. 
A social science student records the angle of each turn before the next 100 steps are taken. 
Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86]. 
(Positive angles are counter-clockwise.) 
Use a turtle to draw the path taken by our drunk friend.'''


import turtle

pirate = turtle.Turtle() #creates the turtle object
pirate.color('green')
pirate.pensize(5)

angles = [160,-43,270,-97,-43,200,-940,17,-86] # creating a list of collected data
direction = 0 

for i in angles:      # iterate through the list
    pirate.left(i)    # turn left because positive values are anticlockwise
    pirate.forward(100)
    direction = i + direction # add up all the angles while looping through the list

print('the pirate is going in ',abs((direction // 360)),'degrees right form the original direction')

