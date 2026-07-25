import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

print("Welcome to the PyPassword Generator!")
numLetters = int(input("How many letters would you like in your password?\n"))
numSymbols = int(input("How many symbols would you like?\n"))
numNumbers = int(input("How many numbers would you like?\n"))

# Letters
password = []
for i in range(numLetters):
   password.append(letters[random.randint(0, len(letters) - 1)])

# Numbers
for i in range(numNumbers):
   password.append(numbers[(random.randint(0, 9))])

# Symbols
for i in range(numSymbols):
    password.append(symbols[random.randint(0, len(symbols) - 1)])


print(password)
random.shuffle(password)
print(password)


    
      

