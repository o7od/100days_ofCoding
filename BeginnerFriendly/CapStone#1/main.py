###################### BlackJack, a capstone project ######################
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## function that draws cards
def draw_card(list_of_cards):
    """
    Returns a random card from the deck
    """
    if len(list_of_cards) < 2:
        for i in range(2):
            num = random.choice(cards)
            list_of_cards.append(num)
    # otherwise, we add just one card to the hand
    else:
        num = num = random.choice(cards)
        if num == 11 and calculate_score(list_of_cards) + num > 21:
            num = 1
        list_of_cards.append(num)

## calculates hands
def calculate_score(hand):
    return sum(hand)

## prints outcome
def final_score(user_hand, computer_hand):
    print(f"Your final hand: {user_hand}, final score: {calculate_score(user_hand)}")
    print(f"Computer's final hand: {computer_hand}, final score: {calculate_score(computer_hand)}")

## shows the status of each hand
def show_status(user_hand, computer_hand):
    print(f"Your cards: {user_hand}, current score: {calculate_score(user_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")

def restatus(hand):
    if calculate_score(hand) > 21 and 11 in hand:
            given_index = hand.index(11)
            hand.pop(given_index)
            hand.insert(given_index, 1)


######### WE START HERE #########
game_start = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
while game_start == 'y':
    ## user attributes
    user_cards = []
    ## computer attributes
    computer_cards = []

    ## randomly get two cards for a user
    draw_card(user_cards)
    draw_card(computer_cards)
    ## show status
    show_status(user_cards, computer_cards)

    ## ask if they want to pass or get another card
    keep_drawing = input("Type 'y' to get another card, type 'n' to pass: ")
    user_won = False

    while keep_drawing == "y":
        draw_card(user_cards)
        ## if the total score is above 21 and there is 11, we replace it with 1
        restatus(user_cards)

        show_status(user_cards, computer_cards)
        if calculate_score(user_cards) > 21:
            final_score(user_cards, computer_cards)
            print("You went over. You lose")
            user_won = True
            break
        keep_drawing = input("Type 'y' to get another card, type 'n' to pass: ")
        
    
        
    if not user_won:
        ## if the computer score is less than user score keep drawing for computer
        while calculate_score(computer_cards) < 17:
            draw_card(computer_cards)
            restatus(computer_cards)
        final_score(user_cards, computer_cards)
        if calculate_score(computer_cards) > 21:
            print("Computer went over. You win!")
        elif calculate_score(computer_cards) > calculate_score(user_cards):
            print("You lose!")
        elif calculate_score(computer_cards) < calculate_score(user_cards):
            print("You win!")
        else: 
            print("Tie.")

            
    game_start = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")


    
    

    