from turtle import Turtle, Screen
import random

## Setting up the screen
my_screen = Screen()
my_screen.setup(width=500, height=400)

## Asking the user for a bet
def bet_color():
    user_choice = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race: Enter a color: ")
    return user_choice

## Putting all players in the starting position
def start_position(turtles: list[Turtle]):
    for i in range(0, len(turtles)):
        turtles[i].penup()
        turtles[i].setpos(-200, -100 + i*50)
        turtles[i].pendown()


## Randomizing steps for each turtle
def random_steps(t: Turtle):
    step = random.randint(10, 40)
    t.penup()
    t.forward(step)
    t.pendown()


## Setting up players
def start_players():
    turtle_colors = ["blue", "green", "yellow", "pink", "brown", "red"]
    all_players = []

    for color in turtle_colors:
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.color(color)
        turtle.turtlesize(1.5, 1.5)
        all_players.append(turtle)

    return all_players


def move_players(players: list[Turtle]):
    game_finished = False
    for player in players:
        if player.xcor() > 200:
            game_finished = True
            return (game_finished, player)
        else:
            random_steps(player)
    return (game_finished, None)


## Starting the Game 
user_bet = bet_color()
players = start_players()
start_position(players)

game_is_finished = False
while not game_is_finished:
    current_game_status = move_players(players)
    game_is_finished = current_game_status[0]
    winner = current_game_status[1]

winner_turtle = winner.pencolor()
if winner_turtle == user_bet:
    print(f"Congratulations! {winner_turtle} turtle won the race!")
else:
    print(f"You lose! {winner_turtle} turtle won the race!")


my_screen.exitonclick()