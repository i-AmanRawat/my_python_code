from turtle import Turtle

class Layout (Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,300)
        self.pendown()
        self.hideturtle()
        self.goto(0,-300)
