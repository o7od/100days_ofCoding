from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -270)
        self.start()

    def go_forward(self):
        self.penup()
        self.forward(20)

    def start(self):
        self.setheading(90)
        self.goto(0, -270)

        