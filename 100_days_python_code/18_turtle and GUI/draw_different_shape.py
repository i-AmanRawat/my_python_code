from turtle import Turtle, Screen
import random

def draw_shape(sides):
    angle = 360/sides
    timmy.forward(100)
    timmy.right(angle)

def colour() :
    list_of_color = ['dark magenta', 'black', 'dark red', 'dark slate grey', 'maroon', 'dark slate blue']
    return random.choice(list_of_color)

timmy= Turtle()
for side_n in range(3,11):
    timmy.color(colour())
    draw_shape(side_n)
    
    
