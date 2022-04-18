from turtle import Turtle,Screen

import random
colors = ["red","orange","yellow","green","blue","purple"]
screen = Screen()
screen.setup(width = 700,height = 500)
user_bet = screen.textinput(title="Make your bet",prompt="Which color turtle will win the race? Enter the color")

x = -330
y=-125
is_race_on = False
#init turtle object
all_turtles = []
for i in range(0,len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=x,y=y)
    y= y+50
    all_turtles.append(new_turtle)
    
if user_bet :
    is_race_on = True

while is_race_on :
  
    for turtle in all_turtles :
        if(turtle.xcor()>330):
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print(f"You've won! The {winning_color} turtle is the winner!")
            else :
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    


# tur1 = Turtle(shape="turtle")
# tur1.penup()
# tur1.color(colors[0])
# tur1.goto(x=-330,y=-125)

# tur2 = Turtle(shape="turtle")
# tur2.penup()
# tur2.color(colors[1])
# tur2.goto(x=-330,y=-75)

# tur3 = Turtle(shape="turtle")
# tur3.penup()
# tur3.color(colors[2])
# tur3.goto(x=-330,y=-25)

# tur4 = Turtle(shape="turtle")
# tur4.penup()
# tur4.color(colors[3])
# tur4.goto(x=-330,y=25)

# tur5 = Turtle(shape="turtle")
# tur5.penup()
# tur5.color(colors[4])
# tur5.goto(x=-330,y=75)

# tur6 = Turtle(shape="turtle")
# tur6.penup()
# tur6.color(colors[5])
# tur6.goto(x=-330,y=125)

























screen.exitonclick()