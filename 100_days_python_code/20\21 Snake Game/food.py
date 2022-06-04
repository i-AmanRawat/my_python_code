from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()  # CALLING THE CONSTRUCTOR OF SUPER CLASSS
        self.shape("circle")  # ADDING SOME MORE FUNCTIONALITY
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(10)
        self.refresh()

    def refresh(self):      #random deployment of food on the screen
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

