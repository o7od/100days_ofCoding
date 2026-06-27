#################### Dictionaries, Nesting ####################

## to create a dictionary
# programming_dictionary = {
#     "Bug": "an error that prevents the computer from running properly", 
#     "Function": "A piece of code that you use to achieve something",
#     "Loop": "The function of doing something over and over again", 
#     }

# print(programming_dictionary["Bug"])
# ## to avoid KeyError, use get('key')
# print(programming_dictionary.get("BBOgug"))
# ## to add, use a new key and assign a value
# programming_dictionary["Compiler"] = "a program that translates the syntax code into a low-level machine code"
# print(programming_dictionary)

# ## to get a list of keys
# print(list(programming_dictionary))

## Looping through a dictionary
# for (key, value) in programming_dictionary.items():
#     print(key, value)

# for item in programming_dictionary:
#     print(programming_dictionary[item])

# ## to an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

## Nesting Lists and Dictionaries
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# travel_log = {
#     "France": ["Paris", "lille", "Dijon"],
#     "Germany": ["Stutgart", "Berlin"],
# }

## Printing Lille
# cities = travel_log["France"]
# print(cities[1])

## nested list
# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])


# ## Nested Dictionaries
# travel_log = {
#     "France": {
#         "num_times_visited": 8,
#         "cities_visited": ["Paris", "lille", "Dijon"],
#     },
#     "Germany": {
#         "cities_visited": ["Stutgart", "Berlin"],
#         "total_visits": 5,
#     }
# }
# print(travel_log["France"]["num_times_visited"])

############################ Secret Auction Game ############################
import BeginnerFriendly.SecretAuction.art as art
print(art.logo)

def find_highest_bidder(bidder_dictionary):
        highest_amount = 0
        winnerName = ""
        for (name, amount) in bidder_dictionary.items():
            if highest_amount < amount:
                highest_amount = amount
                winnerName = name
        
        print(f"The winner is {winnerName} with a bid amount of ${highest_amount}.")


## creating two empty dictionaries
bidders = {}
winner = {}


while True:
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bidders[name] = bid_amount
    next = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if next == "yes":
        print("\n" * 20)
        continue
    else:
        ## if there are no bidders left, we announce the winner
        find_highest_bidder(bidders)
        break



