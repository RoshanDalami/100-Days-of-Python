import turtle as t
import random
tur = t.Turtle()
t.colormode(255)
directions = [0,90,180,270]
# colors = ["medium violet red","purple","dark magenta","violet","magenta","dark orchid"]
tur.pensize(15)
tur.speed("fastest")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tup = (r,g,b)
    return tup
for _ in range(300):
    tur.forward(30)
    tur.color(random_color())
    tur.setheading(random.choice(directions))








screen = t.Screen()
screen.exitonclick()