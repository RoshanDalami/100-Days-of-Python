from cgitb import text
from tkinter import *
from turtle import pd, width
from tkinter import messagebox
import random
import pyperclip  # for copy and paste on the thing
is_ok = False

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(letters) for _ in range(nr_symbols)]
    password_numbers = [random.choice(letters) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    passwords = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password.insert(0,passwords)
    pyperclip.copy(passwords)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global is_ok
    global website
    global email
    global password
    website_entry = website.get()
    email_entry = email.get()
    password_entry  = password.get()
    if((len(website_entry)==0)or (len(email_entry)==0)or (len(password_entry)==0)):
        
        messagebox.showerror(title="Oops",message="You cann't leave any field empty")
        is_ok = False
    else :
        
        is_ok = messagebox.askokcancel(title=f"{website_entry}",message=f"Information Entred are :\n Email: {email_entry} \n Password : {password_entry}")
    

    if is_ok :
        with open("data.txt","a") as data_file:
            data_file.write(f"{website_entry} | {email_entry} | {password_entry}\n")
            website.delete(0,END)
            password.delete(0,END)
            

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)





#Canvas

canvas = Canvas(height=200 , width= 200  )
#image
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= lock_img)
canvas.grid(column=2,row=0)
#Lables 
label_website = Label(text="Website :")
label_website.grid(column=1,row=1)


label_email = Label(text="Email/Username :")
label_email.grid(column=1,row=2)

label_password = Label(text="Password :")
label_password.grid(column=1,row=3)


# Inputs
website = Entry(width=36)
website.grid(column=2, row=1,columnspan=2)
website.focus()

email = Entry(width=36)
email.grid(column=2,row=2,columnspan=2)
email.insert(0,"roshandalami0@gmail.com")

password = Entry(width=21)
password.grid(column=2,row=3)

#Buttons
password_gen = Button(text="generate password",command=generate_password)
password_gen.grid(column=3,row=3)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=2,row=4,columnspan=2)




window.mainloop()