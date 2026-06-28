# import another

# print(another.variable)

# from turtle import Turtle, Screen

# mpabbe = Turtle()
# print(mpabbe)


# my_screen = Screen()

# print(my_screen.canvheight)
# mpabbe.shape("turtle")
# mpabbe.color("green")
# mpabbe.forward(100)

# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = 'l'
# table.align["Type"] = 'c'
# print(table.get_string(2, 3))


# print(table)


class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "Ozod")
user_2 = User("002", "Abliyor")


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
