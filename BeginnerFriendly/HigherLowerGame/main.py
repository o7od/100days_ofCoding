from BeginnerFriendly.HigherLowerGame.game_data import data
from BeginnerFriendly.HigherLowerGame.art import logo, vs
import random


    
def random_celeb():
    return random.choice(data)

def compare(a, b):
    if a["followerCount"] > b["followerCount"]:
        return True
    else:
        return False

def answer(human_response, a_variant, b_variant):
    if human_response == "a":
        return compare(a_variant, b_variant)
    else:
        return compare(b_variant, a_variant)
        


def higher_lower_game():
    game_status = True
    person_a = random_celeb()
    game_score = 0
    print(logo)

    while game_status:
        ## Choosing two random dictionary entries
        person_b = random_celeb()
        if person_b == person_a:
            person_b = random_celeb()

        ## Displaying who is being compared
        print(f'Compare A: {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}.')
        print(vs)
        print(f'Compare B: {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}.')
        
        response = input("Which has more followers? Type 'A' or 'B': ").lower()

        if answer(response, person_a, person_b):
            person_a = person_b
            game_score += 1
            print(logo)
            print(f"You're right! Current score: {game_score}")
        else:
            print(f"Sorry, that's wrong. Final Score: {game_score}")
            game_status = False
    

higher_lower_game()




