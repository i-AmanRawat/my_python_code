from tkinter import *   #only import class and constants but do not import(s) modules
from tkinter import messagebox  #module
from random import randint, choice, shuffle
import pyperclip    #helps in copying content to the clip board
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters= [choice(letters) for _ in range(randint(8, 10))]      #generating random number of word
    password_symbols= [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers= [choice(numbers) for _ in range(randint(2, 4))]

    password_list=password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password= "".join(password_list)
    enter_password.insert(0, string=password)   #inserting the password to the entry box
    pyperclip.copy(password)    #copying password to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website= enter_website.get()
    username= enter_username.get()
    password= enter_password.get()
    #if any entery box is left empty pop window by delievering messaging
    if len(website.strip())==0 or len(username.strip())==0 or len(password.strip())==0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any fields empty!")

    else:
        is_ok= messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {username} \n"
                                                             f"Password: {password} \n")
        if is_ok:
            with open("passwords.txt", "a") as password_file:
                password_file.write(f"{website} | {username} | {password}\n")   #writting password into the file
                enter_password.delete(0, END)   #once details are appended deleter them from 0 to end
                enter_website.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title( "Password Manager")
window.config(padx=50, pady=50)

canva = Canvas(width=200, height=200)
illustration= PhotoImage(file="logo.png")
canva.create_image(120, 100, image= illustration)
canva.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

enter_website = Entry(width=35)
enter_website.focus()
enter_website.grid(column=1, row=1, columnspan=2, sticky="nsew")

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

enter_username = Entry(width=35)
enter_username.insert(0, string= 'example@gmail.com')
enter_username.grid(column=1, row=2, columnspan=2, sticky="nsew")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

enter_password = Entry(width=21)
enter_password.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command= save)
add_button.grid(column=1, row=4, columnspan=2)      #columnspan for how long columns do you want to streach your box


window.mainloop()
