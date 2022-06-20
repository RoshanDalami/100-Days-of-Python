
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=500)

#Entry 
input = Entry(width=10)
input.grid(column=1,row=0)

#Label 1
my_label = Label(text="Miles")
my_label.grid(column=2,row=0)

#Label 2
my_label2 = Label(text="is equal to ")
my_label2.grid(column=0,row=1)
#label 3 
my_label3 = Label(text="0")
my_label3.grid(column=1,row=1)

km = 0
#label4
my_label4 = Label(text="Km")
my_label4.grid(column=2,row=1)
# fucntion to calculate
def calculate():
    user_input = input.get()
    km = float(user_input )* 1.60934
    my_label3.config(text=km)

#button 
button = Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)



window.mainloop()