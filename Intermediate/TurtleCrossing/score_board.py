from turtle import Turtle

FONT = ('Times New Roman', 30, 'normal')


class Score(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.level = 0
        self.create_board()


    def create_board(self):
        self.penup()
        self.hideturtle()
        self.goto(-260, 250)
        self.update_board()


    def update_board(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="Game Over", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_board()

    