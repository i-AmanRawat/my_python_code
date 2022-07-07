import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer= None
# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global rep
    rep=0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    tick_mark.config(text="")
    canva.itemconfig(canva_text, text= "00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if (rep % 8 == 0):
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif (rep % 2 == 0):
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # label.config()    config is used for label not for canvas for canvas we will use itemconfig()
    global timer
    global ticks
    count_min = math.floor(count/60)
    count_sec = count % 60
    if  count_sec<=9:
        count_sec=f"0{count_sec}"

    canva.itemconfig(canva_text, text=f"{count_min}:{count_sec}")
    if (count>0):
        timer= window.after(1000, count_down, count-1)     #after works for milli sec  1sec = 1000
    else :
        start_timer()
        ticks= " "
        work_session= math.floor(rep/2)
        for _ in range(work_session) :
            ticks+="✔︎"
        tick_mark.config(text=ticks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")    ##pomodoro means tomato in italian
window.config(padx=100, pady=50, bg=YELLOW)

timer_label= Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
timer_label.grid(column=1, row=0)

canva = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png= PhotoImage(file="tomato.png")
canva.create_image(100, 112, image =tomato_png)
canva_text= canva.create_text(100, 130, text="00:00", font=(FONT_NAME,35,"bold"))
canva.grid(column=1, row=1)

start= Button(text="Start", bg="white", highlightcolor="white", highlightthickness=2, highlightbackground="white", font=(FONT_NAME, 20, "normal"), command=start_timer)
start.grid(column=0, row=2)

reset= Button(text="Reset", bg="white", highlightcolor="white", highlightthickness=2, highlightbackground="white", font=(FONT_NAME, 20, "normal"), command= timer_reset)
reset.grid(column=2, row=2)

tick_mark= Label( fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))
tick_mark.grid(column=1, row=3)

window.mainloop()   #mainloop() just keep an eye on the screen , does something happen? does something happen ?


'''
    In tkinter don't use while True which runs forever (or runs longer time) because it blocks mainloop() in tkinter 
    and it can't update items in window, and it looks like it freezes. The same problem makes sleep() - it can block 
     mainloop() in tkinter . to run some function with delay - so it can be used like sleep() .
'''








