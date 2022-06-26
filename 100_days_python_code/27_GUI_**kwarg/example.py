from tkinter import *

def buttom_clicked():
    # my_label["text"] = input.get()
    my_label.config(text=input.get())

window= Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

##  LABEL

my_label= Label(text="I am a Label", font=("arial", 20))
# my_label.pack(expand=True)
my_label.grid(column=0, row=0)

# my_label["text"]= "I got clicked"
# my_label.config(text= "I got clicked")

##  BUTTON
button1= Button(text= "Click Me", command=buttom_clicked)
button1.grid(column=1, row=1)

button2= Button(text="new button", command=buttom_clicked)
button2.grid(column=2, row=0)

##  ENTRY
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()

"""
what if no widget manager is specified then widget won't display on the window 
tkinter has many package managers 
we are going to look 3 from them ie
1.pack ->put the widgets one by one using side parameter we place the widgets on left right top and bottom only 
2.place ->all about precise positioning uses coordinate ie somthing that was missing with pack
3.grid ->divides the window in grid and take column and row number the place widget 

in the same program you can't mess the code by using pack after using grid it will throw error 

"""
