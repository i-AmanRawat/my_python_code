from turtle import Turtle
SPEED = [100,200,10,0,20,30,40]
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self,m,n):
        new_xcor= self.xcor() + m*self.x_move
        new_ycor= self.ycor() + n*self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self): #collision with paddle
        self.x_move*=-1
        self.move_speed*=0.9 #multiplying speed of ball with 0.9 every time it goes on a collision

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed= 0.1    #reseting the speed to its original value ie 0.1

    # def random_speed(self):   it doesn't matter how much your speed is at the end there will be sleep line 31
    #     self.speed(random.choice(SPEED))  instead try to reduce the sleep time




