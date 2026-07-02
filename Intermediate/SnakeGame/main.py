from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time



### 1. Setting up the screen
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor(0, 0, 0)
my_screen.title("My Snake Game")

my_screen.tracer(0)
## Creating a Snake Body
snake = Snake()
food = Food()
score = Score()

## Controling snake direction
my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")


## Move the snake body
game_is_on = True
while game_is_on:
    score.update_scoreboard()
    my_screen.update()
    time.sleep(0.1)

    ## Detecting collision with the wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor > 280 or x_cor < -290 or y_cor > 280 or y_cor < -280:
        score.reset()
        snake.reset()
    
    ## Detecting collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    
    ## Detecting collision with the tail
    if snake.contact_with_tail():
        score.reset()
        snake.reset()


    snake.move()






my_screen.exitonclick()