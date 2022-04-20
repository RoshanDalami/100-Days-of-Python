from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake :
    def __init__(self):
        self.starting_positions = [(0,0),(-20,0),(-40,0)]
        self.segments =[]
        
        for position in self.starting_positions:
            self.add_segment(position)
        self.head = self.segments[0]
        self.tail = self.segments[1:]

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            self.new_x = self.segments[seg_num-1].xcor()
            self.new_y = self.segments[seg_num-1].ycor()
        
            self.segments[seg_num].goto(self.new_x,self.new_y)
        self.segments[0].fd(20)
    
    def add_segment(self,position):
        self.new_segment = Turtle("square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.goto(position)
        self.segments.append(self.new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
