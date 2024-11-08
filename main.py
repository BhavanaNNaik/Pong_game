from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Score
import time

paddle = Turtle()

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

game_on = True

target_score=2

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    if score.l_score == target_score or score.r_score == target_score:
        time.sleep(0.1)
        game_on = False
        screen.update()
        time.sleep(0.1)
        score.game_over()  # Display "Game Over" message

screen.exitonclick()
