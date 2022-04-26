from turtle import Turtle 
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        for _ in range(20):
            self.shape("square")
            self.penup()
            self.shapesize(stretch_wid= 1,stretch_len=2.5)
            self.color(random.choice(COLORS))
            self.goto()   
    
        
    
    
