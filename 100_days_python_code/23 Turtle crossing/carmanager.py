from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_collection=[]

    def create_car(self):
        random_chance = random.randint(1, 6)    #generate a new car only every 6th time the game loop runs
        if (random_chance == 1):    #P(E) of 1 is 1/6
            new_car = Turtle("square")
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_collection.append(new_car)

    def move(self):
        for car in self.car_collection:
            if (car.xcor()>-400):
                car.goto(car.xcor()-STARTING_MOVE_DISTANCE, car.ycor())
