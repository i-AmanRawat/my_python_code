"""
import turtle

from turtle import Turtle   #for and import --> to include specific method

from turtle import *    # * --> astersic is used to include all the methods of the turtle

import turtle as t  #aaliasing the turtle module

"""
from turtle import Turtle , Screen
jack = Turtle()     #defining object of turtle classs
# jack.shape("turtle")        #for shapes
jack.color("dark green")    #for color
# jack.dot(50)    #dot(size , color) for dash lines
# jack.setfillcapacity(50)
# jack.forward(100)   #direction of motion
for i in range (30):
    jack.pendown()
    jack.forward(5)
    jack.penup()
    jack.forward(5)


display = Screen()
display.exitonclick()




