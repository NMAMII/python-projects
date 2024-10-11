import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')

paddle_r = Paddle(350)
paddle_l = Paddle(-350)
ball = Ball()
score = ScoreBoard()
screen.listen()
screen.onkey(paddle_l.move_paddle_up, 'w')
screen.onkey(paddle_l.move_paddle_down, 's')
screen.onkey(paddle_r.move_paddle_up, 'Up')
screen.onkey(paddle_r.move_paddle_down, 'Down')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle_r) < 30 and ball.xcor() > 330:
        ball.bounce_paddle()

    if ball.distance(paddle_l) < 30 and ball.xcor() < -330:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()
screen.exitonclick()
