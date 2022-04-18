from turtle import Turtle , Screen

tur = Turtle()

def move_forward():
    tur.fd(10)
screen = Screen()
screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()
