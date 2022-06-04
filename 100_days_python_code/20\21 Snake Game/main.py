import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.tracer(0)    #0 --> screen tracer is off now we will use update() to update manually

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen() #start listen to the instructions
screen.onkey(snake.up, "Up")    #setting up the arrows key
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)     #between two slides maintain delay of 0.1 sec
    snake.move()

    #DETECT COLLISION WITH FOOF
    if snake.head.distance(food) <20:   #distance() --> head and food turtle k bich ki distance ko continously track krra hai
        food.refresh()  #continously deploying food on the screen
        snake.extend()  #extend part of snake after eataing food
        scoreboard.update_score()

    #DETECT COLLISION WITH WALL
    if snake.head.xcor()>280 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-290 :
        scoreboard.game_over()
        game_is_on = False  #end

    #DETECT COLLISION WTIH TAIL
    # for part_of_snake in snake.parts_of_snake :
    #     if part_of_snake != snake.head :
    #         if snake.head.distance(part_of_snake) <15 :
    #             game_is_on= False
    #             scoreboard.game_over()
                #OR
    for part_of_snake in snake.parts_of_snake[1::1]:    #using slicing we excluded head of snake ie first block of snake
        if snake.head.distance(part_of_snake) <15 :
            game_is_on= False
            scoreboard.game_over()

screen.exitonclick()
