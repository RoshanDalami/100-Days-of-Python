from turtle import Turtle , Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard
screen = Screen()
screen.tracer(0)
screen.setup(width=600,height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")


# x=0
# y=0
# collection_turtle = []
# for i in range(0,4):
#     tur = Turtle("square")
#     tur.penup()
#     tur.color("white")
#     tur.goto(x=x,y=y)
#     x=x-20
#     collection_turtle.append(tur)

# starting_positions = [(0,0),(-20,0),(-40,0)]
# segments =[]
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
snake = Snake()
food = Food()
score_board = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()
    


    #detecting collision with food
    # can be done with distance mehtod of turtle class
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
        
        
    #DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_is_on = False
        score_board.game_over()

  
    #detect collision with tail
    # if head collides with any segment in the tail :
    # trigger game_over
    for segment in snake.segments[1:]:
        # if segment == snake.head :
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()













screen.exitonclick()
