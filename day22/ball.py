from turtle import Turtle , Screen
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_cor = 10
        self.y_cor = 10
    def move(self):
        self.new_x = self.xcor() + self.x_cor
        self.new_y = self.ycor() + self.y_cor
        self.goto(self.new_x,self.new_y) 
    def bounce_y(self):
        self.y_cor = self.y_cor * -1
    def bounce_x(self):
        self.x_cor = self.x_cor * -1
       
    



