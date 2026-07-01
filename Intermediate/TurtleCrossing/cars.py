from turtle import Turtle
import random

COLORS_OF_CARS = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "cyan",
    "magenta",
    "gold",
    "royalblue"
]

MOVING_SPEED = 8
X_STARTING_POS = 300    

class Cars():
    def __init__(self):
        self.cars = []
        self.create_car()
        self.car_speed = 0.1


    def create_car(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS_OF_CARS))
        car.setheading(180)
        y_starting_pos = random.randint(-260, 260)
        car.goto(X_STARTING_POS, y_starting_pos)
        self.cars.append(car)

    
    def move(self):
        for each_car in self.cars:
            each_car.forward(8)

    def hit_player(self, player: Turtle):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
    

    def remove_cars(self):
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)
                car.hideturtle()

    def update_speed(self):
        self.car_speed *= 0.9


        