from turtle import Turtle
FONT = ('Arial', 14, 'normal')
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.clear()
        self.hideturtle()
        self.score_board_update()
    def score_reader(self):
        with open("data.txt",mode="w") as data:
            data.write(str(self.high_score))
    def score_board_update(self):
        with open("data.txt") as data:
            self.highScore = data.read()
        self.clear()
        self.write(f"score : {self.score} High Score : {self.highScore}",align = ALIGNMENT,font=FONT)

    def reset(self):
        if(self.score > self.high_score):
            self.high_score = self.score
            self.score_reader()
        self.score = 0
        self.score_board_update()
       
    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.score_board_update() 
