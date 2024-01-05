from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

obj = Turtle()

colours = ["red","blue","green"]

#draw a square:
'''for i in range(4):
    obj.forward(100)
    obj.right(90)'''

#draw a dashed line:

'''for i in range(15):
    obj.pendown()
    obj.forward(10)
    obj.penup()
    obj.forward(10)'''
# generate triangle to decagon:
'''for i in range(3,11):
    angle=360/i

    for j in range(i):
        obj.forward(100)
        obj.right(angle)'''

# draw random walk:
'''
directions=["left","right","straight"]

obj.speed(9)
obj.width(10)

for i in range(250):
    direction_of_obj= random.choice(directions)
    random_colour= (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    obj.color(random_colour)


    if direction_of_obj=="left":
        obj.left(90)
    elif direction_of_obj=="right":
        obj.right(90)

    obj.forward(25) '''


#draw a spirograph:

pos = obj.heading()
obj.speed("fastest")
obj.circle(100)
obj.setheading(pos+20)

while(obj.heading()!=pos):

    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255 ))
    obj.color(color)

    obj.circle(100)
    obj.setheading(obj.heading()+5)


    
    







screen = Screen()
screen.exitonclick()
