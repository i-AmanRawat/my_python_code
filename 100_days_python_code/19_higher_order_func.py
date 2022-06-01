'''

    higher order function :     --> func_B is a higher order function

    def func_A (a):
        do this with a ;

    def func_B (b, func_A):     --> one thing to keep in mind is do not pass paranthesis with func_A
        do this with b and func_A;

'''
from turtle import Turtle, Screen

def move_forward():
    tim.forward(100)

def move_backward():
    tim.backward(100)

def move_anticlockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clear_drawing():
    screen.resetscreen()

tim = Turtle ()
screen = Screen ()
screen.listen ()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(move_anticlockwise, 'a')
screen.onkey(move_clockwise, 'd')
screen.onkey(clear_drawing, 'c')
screen.exitonclick()
