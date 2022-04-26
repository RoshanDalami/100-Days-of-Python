from turtle import Turtle 

class Paddle(Turtle) :

    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.paddle = Turtle("square")
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid = 5,stretch_len = 1)
        self.paddle.goto(self.x_cor,self.y_cor)

    def move_up(self):
        self.y_cor = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(),self.y_cor) 
    def move_down(self):
        self.y_cor = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(),self.y_cor)

