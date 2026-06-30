from turtle import Turtle, Screen
from players import Players
from ball import Ball
from score import Score
import time


# 1. Setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor(0, 0, 0)
screen.title("Pong")


# 2. Creating a player object for a user
screen.tracer(0)
r_paddle = Players((350, 0))
l_paddle = Players((-350, 0))



# 3. Listening to keys
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# 4. Creating a ball
ball = Ball()

# 5. Creating a scoreboard
score = Score()



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    ## Detecting collision with the wall
    if ball.hit_wall():
        ball.change_y_direction()

    ## Detecting collision with the paddles
    if ball.distance(r_paddle) < 30 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.change_x_direction()


    ## Detecing if the ball passed the paddles
    if ball.pass_r_paddle():
        score.l_score += 1
        ball.reball()
    elif ball.pass_l_paddle():
        score.r_score += 1
        ball.reball()

    score.update_score()
        



screen.exitonclick()