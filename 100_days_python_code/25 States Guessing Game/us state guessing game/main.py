from turtle import Screen, Turtle
import pandas
data= pandas.read_csv("50_states.csv")  #converting the csv data into a dataframe

screen= Screen()
screen.title("U.S. States Guessing Game")
image= "blank_states_img.gif"
screen.addshape(image)  #adding the shape to its turtle
jim= Turtle()   #for gif
jerry= Turtle()     #for writting the states name
jerry.penup()
jim.shape(image)     #making turtle of the shape we have added

correct_answer= 0
data.set_index("state")     #setting the name of state as index column to make it easy to delete a particular row from dataframe once the guess is right
while len(data)>0:  #run loop till all 50 states are convered
    answer_state= screen.textinput(title= f"{correct_answer}/50 States Correct", prompt="What's another state name?").title()    #creating a small text input window for guessing the state and storing that name
    row = (data[data['state']==answer_state])   #matching weather the your answered state exist or not

    if (answer_state=="Exit"):      #giving the user access in case (s)he wants to exit the game
        break
    if (len(row)==1):       #if the answered state will match then length of row will become 1
        correct_answer+=1
        x_cor= int(row['x'])    #fetching x and y coordinate to palce the name of state on the map
        y_cor= int(row['y'])
        jerry.goto(x_cor, y_cor)    #mapping the name of state
        jerry.write(answer_state.title(), font=("Verdana",10, "normal") )
        data.drop(row.index,  axis=0, inplace=True)     #removing the answered state from the dataframe so that we won't match it again
data.to_csv("states_to_learn.csv")      #converting the left states in dataframe into csv file so that the player could learn the unguessed name of states