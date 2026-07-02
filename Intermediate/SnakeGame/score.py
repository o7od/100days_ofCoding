from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # we first write our high score to the score.txt file 
        with open("scores.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # with open("scores.txt") as score_file:
        #     self.high_score = int(score_file.read())
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # here, we should update the score
            with open("scores.txt", mode="w") as score_file:
                score_file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.penup()
    #     self.home()
    #     self.color("white")
    #     self.hideturtle()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)