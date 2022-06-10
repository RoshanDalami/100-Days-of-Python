from tkinter import *


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=500)


#Label

my_label = Label(text="Hello , I am Roshan Dalami",font=("Arial",24,"bold"))
my_label.config(text="New ")
my_label.grid(column=0,row=0)


#Button
def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input)
button = Button(text="click me" , command=button_clicked)
button.grid(column=1,row=1)


#Entry 
input = Entry(width=10)
input.grid(column=4,row=3)

button1 = Button(text="Click Me 1")
button1.grid(column=3,row=0)









window.mainloop()