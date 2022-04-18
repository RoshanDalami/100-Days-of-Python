# import colorgram 
# rgb_colors = []
# colors = colorgram.extract('usingPicture.jpg',30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tup_color = (r,g,b)
#     rgb_colors.append(tup_color)
import turtle as t
import random
t.colormode(255)
tur = t.Turtle()
tur.speed("fastest")
tur.penup()
tur.hideturtle()
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

tur.setheading(225)
tur.forward(300)
tur.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    tur.dot(20,random.choice(color_list))
    
    tur.forward(50)
    if dot_count % 10 == 0:
        tur.setheading(90)
        tur.forward(50)
        tur.setheading(180)
        tur.forward(500)
        tur.setheading(0)


screen = t.Screen()
screen.exitonclick()