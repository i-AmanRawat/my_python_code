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
    window.after_cancel(flip_timer)
    currennt_card= random.choice(to_learn)
    new_random_french_word= currennt_card['French']
    canvas.itemconfig(word, text=new_random_french_word, fill= "black")
    canvas.itemconfig(title, text="French", fill= "black")
    canvas.itemconfig(card_background, image= card_front_img)
    flip_timer= window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    english_word = currennt_card['English']
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill= "white")

def is_known():
    to_learn.remove(currennt_card)
    data= pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR)
flip_timer= window.after(3000, flip_card)

canvas = Canvas(width = 800, height = 526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img= PhotoImage(file="images/card_back.png")
card_background= canvas.create_image(400, 263, image= card_front_img)
title= canvas.create_text(400, 150, text= "",fill="black" , font=("Ariel", 40, "italic"))
word= canvas.create_text(400, 263, text="",fill="black" , font=("Ariel", 60, "bold"))
canvas.config( bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2 )

no_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=no_image, highlightbackground=BACKGROUND_COLOR, command= next_card)
unknown_button.grid(row=1, column=0)

yes_image = PhotoImage(file="images/right.png")
known_button = Button(image= yes_image, highlightbackground=BACKGROUND_COLOR, command= is_known)
known_button.grid(row= 1, column=1)

next_card()

window.mainloop()