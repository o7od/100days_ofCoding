from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.show_board()

    def update_score(self):
        self.clear()
        self.score += 1

    def show_board(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.home()
        self.color("white")
        self.hideturtle()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)