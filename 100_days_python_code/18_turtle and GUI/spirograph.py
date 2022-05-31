import random
import turtle as t

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r, g, b)
    return rgb

'''
    how to figure out how many number of times the loop/circle need to to be drawn 
    360/degree by which you are rotating here 3
'''
def draw_spirograph():
    degree = int(input("Enter by how much degree you want to rotate : "))
    for i in range(int(360/degree)):
        jim.color(random_color())
        jim.setheading(jim.heading() + degree)
        # jim.circle(100, 360, 4)   //100-->radius  360-->angle of arc to be draw 4-->complete arc in 4 steps# jim.circle(100, 360, 4)   //100-->radius  360-->angle of arc to be draw 4-->complete arc in 4 steps
        jim.circle(radius=100)

jim = t.Turtle ()
jim.pen(pensize=0.1, speed=30)
t.colormode(255)
draw_spirograph()

screen = t.Screen()
screen.exitonclick()

