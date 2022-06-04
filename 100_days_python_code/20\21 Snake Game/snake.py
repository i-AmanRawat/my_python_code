from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20  # PACES
UP = 90
DOWN = 270  # set the direction either in cw or acw follow one convention only will be good for you
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.parts_of_snake = []
        self.create_snake()
        self.head = self.parts_of_snake[0]

    def create_snake(self):
        for POSITION in STARTING_POSITION:
            self.add_part_to_snake(POSITION)

    def add_part_to_snake(self,POSITION):
        jim = Turtle(shape="square")
        jim.color("white")
        jim.penup()
        jim.goto(POSITION)
        self.parts_of_snake.append(jim)

    def extend(self):
        self.add_part_to_snake(self.parts_of_snake[-1].position())  # -1 --> refers to the last part of the snake

    def move(self):
        # for parts in parts_of_snake :
        #     parts.forward(20)
        for i in range(len(self.parts_of_snake) - 1, 0, -1):
            posi_of_pre_part = self.parts_of_snake[i - 1].position()
            self.parts_of_snake[i].goto(posi_of_pre_part)
        self.head.forward(MOVE_DISTANCE)
        # parts_of_snake[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
