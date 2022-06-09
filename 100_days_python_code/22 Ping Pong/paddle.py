from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
            self.turtlesize(stretch_wid=5, stretch_len=1 )    #by default value 20 -20
            self.shape("square")
            self.color("white")
            self.penup()
            self.goto(position)

    def go_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)   #x cordinate will remain same we will only move paddle along y axis

    def go_down(self):
        new_y_cor = self.ycor() +(-20)
        self.goto(self.xcor(), new_y_cor)

