from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

# reading our states.csv document and turning it into a dictionary
states_data = pandas.read_csv("50_states.csv")
states = states_data.to_dict(orient="records")
list_of_states = states_data["state"].to_list()


# Go to x_cor and y_cor and draw
def draw_state(state_name, x_cor, y_cor):
    drawer = Turtle()
    drawer.hideturtle()
    drawer.penup()
    drawer.goto(x_cor, y_cor)
    drawer.write(f"{state_name}", align="center", font=('Arial', 10, 'normal'))


# Saves the states not entered by the user as a csv file
def save_data(user_states, correct_states):
    for state in user_states:
        if state in correct_states:
            correct_states.remove(state)

    data_to_save = {
        "Missed States": correct_states
    }

    df = pandas.DataFrame(data_to_save)
    df.to_csv("missed_states.csv")



guessed_states = []
while len(guessed_states) < 50:
    # Asking the user to guess a state
    answer_state = screen.textinput(f"Guess the state {len(guessed_states)}/50", "Enter a state name").title()

    if answer_state == "Exit":
        save_data(guessed_states, list_of_states)
        break

    # Checking the user answer against the states
    for each_state in states:
        if each_state["state"] == answer_state:
            guessed_states.append(answer_state)
            x_cor = each_state["x"]
            y_cor = each_state["y"]
            draw_state(answer_state, x_cor, y_cor)



screen.mainloop()

