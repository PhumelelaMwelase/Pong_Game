from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # DETECT WALL COLLISION
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECT PADDLE COLLISION
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # DETECT RIGHT PADDLE MISS
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.respawn()

    # DETECT RIGHT PADDLE MISS
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.respawn()


screen.exitonclick()
