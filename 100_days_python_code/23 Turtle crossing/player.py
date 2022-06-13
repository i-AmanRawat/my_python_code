from turtle import Turtle

STARTING_POSITION = (0, -280)
HEADING= 90
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(HEADING)
        self.color("white")
        self.shape("turtle")
        self.initial_position()

    def initial_position(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        y_cor = self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(), y_cor)
