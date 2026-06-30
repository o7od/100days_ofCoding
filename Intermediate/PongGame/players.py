from turtle import Turtle


class Players(Turtle):
    def __init__(self, positions: tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(positions)
    
    
    def up(self):
        y_cor = self.ycor() + 30
        self.goto(self.xcor(), y_cor)
    
    def down(self):
        y_cor = self.ycor() - 30
        self.goto(self.xcor(), y_cor)



