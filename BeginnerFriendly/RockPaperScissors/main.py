# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# # print(dirty_dozen[1][1])

# print(dirty_dozen)
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

## This is to get the rock paper or scissors for the computer
# list = [rock, paper, scissors]

# game_states = False

# while not game_states:
#     ## this will generate a random index between 0 and the length of the list - 1
#     random_int = random.randint(0, len(list) - 1)

#     userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
#     print(list[userInput])

#     print(f"Computer chose: \n{list[random_int]}")

#     ## Logic of the game
#     if userInput == random_int: 
#         continue
#     elif userInput - random_int == 1 or userInput - random_int == -2:
#         print("You win")
#         break
#     elif random_int - userInput == 1 or random_int - userInput == -2:
#         print("game over")
#         break
#     else: 
#         continue

    


