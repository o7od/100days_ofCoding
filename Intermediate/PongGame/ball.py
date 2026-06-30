from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.home()
        self.shape("circle")
        self.color("blue")
        self.change_x = 15
        self.change_y = 15
        self.move_speed = 0.1

    def reball(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.change_x_direction()
    

    def move(self):
        self.goto(self.xcor() + self.change_x, self.ycor() + self.change_y)

    def hit_wall(self):
        if self.ycor() > 0 and self.ycor() > 275:
            return True
        elif self.ycor() < 0 and self.ycor() < -275:
            return True
        return False


    def change_x_direction(self):
        self.move_speed *= 0.9
        self.change_x = -(self.change_x)

    
    def change_y_direction(self):
        self.change_y = -(self.change_y)


    def pass_r_paddle(self):
        return self.xcor() > 380
    
    def pass_l_paddle(self):
        return self.xcor() < -380
     


 