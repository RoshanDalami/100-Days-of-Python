from turtle import Turtle ,Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) #stop the animation

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

ball = Ball()

    
screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")



game_is_on = True

while game_is_on :
    time.sleep(0.1)
    screen.update()
    ball.move()
    #if ball collid with upper wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detecting the collision on the paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor()>340) or (ball.distance(l_paddle) < 50 and ball.xcor()>-340):
        ball.bounce_x()


screen.exitonclick()