from turtle import Turtle, Screen
from player import Player
from cars import Cars
from score_board import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# 1. Creating the player
player = Player()
screen.listen()
screen.onkey(player.go_forward, "Up")

# 2. Creating a car object
car = Cars()
times = 0

# 3. Creating a score board
score = Score()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(car.car_speed)

    # 1. Randomly generating a car on x/y axis
    if times == 5:
        car.create_car()
        times = 0

    # 2. Detecting collision with the car
    if car.hit_player(player):
        score.game_over()
        game_is_on = False

    # 3. If the player reaches the other side, we go to next level
    if player.ycor() > 280:
        score.increase_level()
        player.start()
        car.update_speed()

    
    car.move()
    times += 1

    # Removes the car that left the screen
    car.remove_cars()



screen.exitonclick()
