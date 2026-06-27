################## Number Guessing Game ##################
import random
from BeginnerFriendly.NumberGuessingGame.art import logo

## Global Variables
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Hard mode function
def game_mode(random_number, num_attempts):

    while num_attempts > 0:
        print(f"You have {num_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess > random_number:
            user_guess = print("Too high.\nGuess again.")
        elif user_guess < random_number:
            user_guess = print("Too low.\nGuess again.")
        else:
            print(f"You got it! The answer was {random_number}")
            break
        num_attempts -= 1
        if num_attempts == 0:
            print("You've run out of guesses. Refresh the page to run again! ")
            break


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
    ran_num = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


    if difficulty == "hard":
        game_mode(ran_num, HARD_LEVEL_TURNS)
    else:
        game_mode(ran_num, EASY_LEVEL_TURNS)


game()





