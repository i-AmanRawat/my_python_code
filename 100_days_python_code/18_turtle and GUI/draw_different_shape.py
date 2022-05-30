from turtle import Turtle, Screen
import random

def draw_shape(sides):
    angle = 360/sides
    for i in range(sides):
        timmy.forward(100)
        timmy.right(angle)

def colour() :
    list_of_color = ['dark magenta', 'black', 'dark red', 'dark slate grey', 'maroon', 'dark slate blue']
    return random.choice(list_of_color)

timmy= Turtle()
timmy= Screen()
timmy.exitonclick()
timmy.pen(pensize=3, speed= 10)
for side_n in range(3,11):
    timmy.color(colour())
    draw_shape(side_n)


