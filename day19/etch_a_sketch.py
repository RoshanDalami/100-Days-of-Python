from turtle import Turtle , Screen

tur = Turtle()

def move_forward():
    tur.fd(20)
def move_backward():
    tur.bk(20)
def counter_clockwise():
    tur.left(20)
def clockwise():
    tur.right(20)
def clr_screen():
    tur.reset()
screen = Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clr_screen)


screen.exitonclick()