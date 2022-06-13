from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
#/Users/amanrawat/Downloads/Snake+Project+Code+from+Day+21/main.py
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=0
        with open("/Users/amanrawat/Desktop/highscorefile.txt", mode='r') as highscorefile:
            self.high_score= int(highscorefile.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def highscore(self):
        if (self.score>self.high_score):
            self.high_score=self.score
            with open("/Users/amanrawat/Desktop/highscorefile.txt",mode='w+') as highscorefile :
                highscorefile.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
