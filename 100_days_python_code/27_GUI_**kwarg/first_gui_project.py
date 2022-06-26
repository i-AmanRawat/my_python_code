from tkinter import *

def calculate():
    dis_in_km= float(input_miles.get())*1.60934
    result_label.config(text=dis_in_km)


window = Tk()
window.minsize(width=150, height=100)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

##  entery
input_miles= Entry()
input_miles.config(width=7)
input_miles.grid(column=1, row=0)

##  LABEL
miles_label= Label(text="Miles", font=("arial", 15))
miles_label.grid(column=2, row=0)

is_equal_to_label= Label(text="is equal to ", font=("arial", 15))
is_equal_to_label.grid(column=0, row=1)

result_label = Label(text="0", font=("arial", 15))
result_label.config(padx=7)
result_label.grid(column=1, row=1)

km= Label(text="Km", font=("arial", 15))
km.grid(column=2, row=1)

##  BUTTON
calculate_button= Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)





window.mainloop()
