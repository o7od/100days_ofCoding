print("Welcome to Treasure Island")

first_operation = input("You are at a cross road. Where do you want to go? left or right?").lower()


if first_operation == "right":
    print("Game Over")
else:
    second_input = input("Swim or Wait").lower()
    if second_input == "swim":
        print("game over")
    else:
        final_input = input("Which door").lower()
        if final_input == "red" or final_input == "blue":
            print("Game Over")
        elif final_input == "yellow":
            print("you win!")
        else:
            print("Game Over")

