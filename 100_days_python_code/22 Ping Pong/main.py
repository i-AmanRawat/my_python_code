from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from layout import Layout
import time

L_POSITION = (-350, 0)
R_POSITION = (350, 0)

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.title("Ping Pong")
screen.tracer(0)

l_paddle = Paddle(L_POSITION)
r_paddle = Paddle(R_POSITION)
ball = Ball()
scoreboard= ScoreBoard()
layout = Layout()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

m, n= 1, 1
game_is_on = True
while game_is_on:
    ball.move(m,n)
    time.sleep(ball.move_speed)
    screen.update()

    #DETECTING COLLISION WITH WALL AND BOUNCE
    if (ball.ycor()>280 or ball.ycor()<-280):
        ball.bounce_y()       #vertical bounce

    #DETECTING COLLISION WITH PADDLE AND BOUNCE
    if (ball.xcor()>320 and ball.distance(r_paddle)<50 or ball.xcor()<-320 and ball.distance(l_paddle)<50) :
        ball.bounce_x()        #horizontal bounce

    #DETECT WHEN RIGHT PADDLE MISSES
    if (ball.xcor()>380 and ball.distance(r_paddle)>50 ) :
        ball.reset_position()
        scoreboard.l_point()
        time.sleep(0.5)
        m=-1
        n=-1

    #DETECT WHEN LEFT PADDLE MISSES
    if (ball.xcor()<-380 and ball.distance(l_paddle)>50) :
        ball.reset_position()
        scoreboard.r_point()
        time.sleep(0.3)
        m=1
        n=1


screen.exitonclick()




# #DETECT COLLISION WITH WALL AND BOUNCE
#     if (ball.ycor() == 300 and ball.xcor()>0):  #RIGHT UPPER WALL
#         m = 1
#         n = -1
#
#     if (ball.ycor() == -300 and ball.xcor()>0): #RIGHT LOWER WALL
#         m = 1
#         n = 1
#
#     if ( ball.xcor()==400):
#         game_is_on=False
#
#     if (ball.ycor() == 300 and ball.xcor()<0):  #LEFT UPPER WALL
#         m=-1
#         n=-1
#
#     if (ball.ycor() == -300 and ball.xcor() < 0):   #LEFT LOWER WALL
#         m = -1
#         n = 1
#
#     if ( ball.xcor()==-400):
#         game_is_on=False
#
#     #DETECTING COLLOSION WITH PADDLE
#     if (ball.distance(r_paddle)<50 and ball.xcor()==340):
#         if(m==1 and n==-1):
#             m=-1
#             n=-1
#         else:
#             m=-1
#             n=1
#
#     if (ball.distance(l_paddle)<50 and ball.xcor()==-340):
#         if(m==-1 and n== 1):
#             m=1
#             n=1
#         else:
#             m=1
#             n=-1
