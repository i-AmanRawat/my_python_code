from tkinter import *

def calculate():
    if (listbox.get(listbox.curselection())=="Kilometers"):
        dis_in_km= float(input_miles.get())*1.60934
        result_label.config(text=dis_in_km)

    elif (listbox.get(listbox.curselection())=="Meters"):
        dis_in_m= float(input_miles.get())*1609.34
        result_label.config(text=dis_in_m)

    elif (listbox.get(listbox.curselection())=="Centimeter"):
        dis_in_cm= float(input_miles.get())*160934
        result_label.config(text=dis_in_cm)     #its same as updating something

    unit_label.config(text=listbox.get(listbox.curselection()))

window = Tk()
window.minsize(width=150, height=100)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)     #seleting up the margin  

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

unit_label= Label(text="Km", font=("arial", 15))
unit_label.grid(column=2, row=1)

##  BUTTON
calculate_button= Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=3)
units = ["Kilometers", "Meters", "Centimeter"]
for unit in units:
    listbox.insert(units.index(unit), unit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.config(width=10)
listbox.grid(column=1, row=4)

window.mainloop()
