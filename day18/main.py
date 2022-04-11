from turtle import Turtle , Screen
import random
tur = Turtle()
tur.pensize(5)
colors = ["medium violet red","purple","dark magenta","violet","magenta","dark orchid"]
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle= 360 / num_sides
        tur.forward(100)
        tur.right(angle)

for color in range(len(colors)):
    tur.color(colors[color])
for shape_side_n in range(3,11):
    tur.color(random.choice(colors))
    draw_shape(shape_side_n)
    
   





screen = Screen()
screen.exitonclick()