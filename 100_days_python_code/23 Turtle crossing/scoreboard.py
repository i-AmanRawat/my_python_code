from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT= "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        self.run_speed=0.1

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level : {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level+=1
        self.run_speed*=0.9
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


