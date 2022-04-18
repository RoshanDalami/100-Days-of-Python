import turtle as t
import random

tur = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tup = (r,g,b)
    return tup
tur.speed("fastest")
def spirograph_draw(size_of_offset):
    for i in range(int(360/size_of_offset)):
        tur.color(random_color())
        tur.circle(100)
        tur.setheading(tur.heading()+size_of_offset)

spirograph_draw(5)










screen = t.Screen()
screen.exitonclick()