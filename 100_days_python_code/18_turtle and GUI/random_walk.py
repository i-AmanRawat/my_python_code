from turtle import Turtle , Screen
import random

def random_motion(cook):
    function_list = [1, 2]
    cook.color(colour())
    if random.choice(function_list)==1 :
        cook.forward(30)
        return 0
    cook.backward(30)

def random_direction(cook):
    direction = [0,90,180,270]
    cook.setheading(random.choice(direction))

def colour() :
    list_of_color = ['dark magenta', 'black', 'dark red', 'dark slate grey', 'maroon', 'dark slate blue',
                     'pale turquoise','gold', 'hot pink', 'lavender blush', 'deep sky blue', 'light gray',
                     'green yellow', 'orange', 'dark salmon']
    return random.choice(list_of_color)

cook= Turtle()
cook.pen(speed=10, pensize=15)

for i in range (400):
    random_motion(cook)
    random_direction(cook)

screen= Screen()
screen.exitonclick()
