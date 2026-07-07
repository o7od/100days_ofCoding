import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']


class PasswordGenerator:
    def __init__(self):
        self.password_list = []
        self.password = ""

    def make_password(self):
        for i in range(0, random.randint(3, 7)):
            self.password_list.append(random.choice(letters))
        
        for i in range(0, random.randint(3, 7)):
            self.password_list.append(random.choice(numbers))
    
        for i in range(0, random.randint(3, 7)):
            self.password_list.append(random.choice(symbols))

        random.shuffle(self.password_list)
        for s in self.password_list:
            self.password += s
    
        return self.password