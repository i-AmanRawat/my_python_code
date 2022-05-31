import random
import turtle as t
#making a list of direction that i can feed inside the setheading() function  but i m using only (90 + theta) direction
direction = [0, 90, 180, 270]
'''
this function will help us generate a random code ranging from 0 to 255 for each r, g, b hence returning the 3 values 
using a tuple.
value of r, g, b represents some amount of red and others as well #primary color
'''
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

tim= t.Turtle()     #object named as tim
tim.pen(speed=10 , pensize=8)       #setting the functioning of the pen max speed 10
t.colormode(255)    #enabling the range from 0 to 255 if we will specify the color code 200 then we will not be able to generate color code of 255
for i in range (500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))    #function which is heading the arrow 

screen = t.Screen()
screen.exitonclick()
