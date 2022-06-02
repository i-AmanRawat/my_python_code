from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color : ")
colors = ["red", "orange", "yellow", "blue", "purple"]      #created a list of colors to assing them to turtles
all_turtles = []          #created empty list to create multiple turtle objects  #"tim", "jerry", "tom", "sandy", "cook"
is_race_on = False

for i in range (len(colors)):
    turtles = Turtle(shape="turtle")
    turtles.color(colors[i])
    turtles.penup()                      #pen will be up otherwise we will see lines on track
    turtles.goto(-230, -100 + i * 50)    #placing all the turtle racers on the starting line
    all_turtles.append(turtles)
if user_bet:        #checking wheather user has placed a bet or not
    is_race_on = True       #if bet is placed lets race
    while is_race_on:

        for turtle_racers in all_turtles:
            if turtle_racers.xcor() > 230 :       #to win the race turtle need to surpas the 230 x cordinate
                winning_color = turtle_racers.pencolor()    #storing the color of winner turtle to later on equate #not using color instead using pencolor bcz color returns 2 arguments
                is_race_on = False      #switching off the while loop
                if winning_color == user_bet:   #checking the bet was equals to the winner or not
                    print(f"You've won ! The {winning_color} turtle is the winner!")
                    break   #bcz what if another coloured turtle is also a winner that y jis ka naam phale aaayega vo winner hoga
                else :
                    print(f"You've lost ! The {winning_color} turtle is the winner!")
            cover_distance = random.randint(0, 10)
            turtle_racers.forward(cover_distance)     #moving the turtles forward one by one (but faster)

screen.exitonclick()
