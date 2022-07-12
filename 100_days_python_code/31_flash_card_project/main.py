from tkinter import *
import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
currennt_card= {}
to_learn=  {}

try:
    data= pd.read_csv("data/words_to_learn.csv")    
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

def next_card():
    global currennt_card, flip_timer
    window.after_cancel(flip_timer)     #cancelling the timer that is running from main 
    currennt_card= random.choice(to_learn)
    new_random_french_word= currennt_card['French']
    canvas.itemconfig(word, text=new_random_french_word, fill= "black")
    canvas.itemconfig(title, text="French", fill= "black")
    canvas.itemconfig(card_background, image= card_front_img)   #bcz once the background change on flipping card then we have to set it back to previous one
    flip_timer= window.after(3000, flip_card)       #setting up new timer to start after every next_card()

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)     #setting the background for the back side of card
    english_word = currennt_card['English']
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill= "white")

def is_known():
    to_learn.remove(currennt_card)      #removing the words we have guessed right 
    data= pandas.DataFrame(to_learn)    #converting the left over to_learn list into DataFrame
    data.to_csv("data/words_to_learn.csv", index= False)    #converting the df into csv but without index
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR)
flip_timer= window.after(3000, flip_card)       #3000ms = 3s 

canvas = Canvas(width = 800, height = 526)
card_front_img = PhotoImage(file="images/card_front.png")       #we will face issue if we will call photoimage inside any of the function 
card_back_img= PhotoImage(file="images/card_back.png")
card_background= canvas.create_image(400, 263, image= card_front_img)
title= canvas.create_text(400, 150, text= "",fill="black" , font=("Ariel", 40, "italic"))
word= canvas.create_text(400, 263, text="",fill="black" , font=("Ariel", 60, "bold"))
canvas.config( bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2 )

no_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=no_image, highlightbackground=BACKGROUND_COLOR, command= next_card)   #if don't know simply call next card ie without deleting the the word displayed from the list 
unknown_button.grid(row=1, column=0)

yes_image = PhotoImage(file="images/right.png")
known_button = Button(image= yes_image, highlightbackground=BACKGROUND_COLOR, command= is_known)    #if you got the correct answer then delete the word from the list then run next_card()
known_button.grid(row= 1, column=1)

next_card()

window.mainloop()
