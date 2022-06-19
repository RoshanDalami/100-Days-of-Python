from email.mime import image
from tkinter import *
import math
from turtle import st
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.itemconfig(timer_text, text= f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)
    


# ---------------------------- COUNTDOWN MECHANISM----------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if(count > 0):
        window.after(1000,count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)




# 1sec = 1000ms
 # window.after() take amount of time it has to wait and take the function to call and passing argumnet you want to 


 
#Timer label
timer_label = Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
timer_label.grid(column=2,row=1)




#to remove the border between window and canvas set highlightthickness = 0
#canvas 
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness = 0)

#photoImage is the method of the tkinter for reading the photo from file
tomato_img = PhotoImage(file="tomato.png")
#create_image is the method in canvas x and y position is required
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,40,"bold"))
canvas.grid(column=2,row=2)



#Button section

#start Button
start_btn = Button(text="Start",highlightthickness = 0 , command= start_timer)

start_btn.grid(column=1,row=3)
#Reset Button

reset_btn = Button(text="Reset",highlightthickness = 0, command=reset_timer)
reset_btn.grid(column=3,row=3)


#Check mark
check_label = Label(text="✔️",bg=YELLOW,fg=GREEN)
check_label.grid(column=2,row=4)












window.mainloop()