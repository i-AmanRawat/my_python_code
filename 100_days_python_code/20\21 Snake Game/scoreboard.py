from turtle import Turtle
ALIGNMENT = "CENTER"    #constant
FONT = ("Arial", 24, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()   #hiding the turtle
        self.write(f"Score : {self.score}", align=ALIGNMENT, font= FONT)    #for writting something on the screen

    def update_score(self):
        self.clear()    #clear() --> clears the content you wrote using write function otherwise it will overwrite on previous content if something is written already on the screen
        self.score+=1
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write("GAME OVER !", align=ALIGNMENT, font=FONT)

