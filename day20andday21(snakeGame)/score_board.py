from turtle import Turtle
FONT = ('Arial', 14, 'normal')
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.clear()
        self.hideturtle()
        self.score_board_update()
    
    def score_board_update(self):
        self.write(f"score : {self.score}",align = ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align = ALIGNMENT,font=FONT)


    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.score_board_update()

