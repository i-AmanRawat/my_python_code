import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard= Scoreboard()
car = CarManager()


screen.listen()
screen.onkey(player.move_up, "Up")  #do not enter paranthesis to the function passed as the arguement

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    #DETECTING COLLISION BETWEEN TURTLE AND CARS
    for cars in car.car_collection:
        if (player.distance(cars) <20):
            scoreboard.game_over()
            game_is_on= False

    #DETECTING PLAYER HAS REACHED OTHER SIDE
    if (player.ycor()>280):
        player.initial_position()
        scoreboard.level_up()



screen.exitonclick()
