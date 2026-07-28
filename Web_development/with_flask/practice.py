# def add(n1, n2):
#     return n1 + n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# def subtract(n1, n2):
#     return n1 - n2


# nesting functions inside functions
# def outer_function():
#     print("i'm outer")

#     def inner_function():
#         print("i'm inner")

#     return inner_function

# result = outer_function()
# result()

### Python Decorator ###
# import time

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         # Do something before
#         function()
#         function()
#         # Do something after

#     return wrapper_function


# @delay_decorator
# def say_hello():
#     print("Hello")

# @delay_decorator
# def say_bye():
#     print("Bye")


# def say_greeting():
#     print("How are you?")


# say_hello()
# decorated_function = delay_decorator(say_greeting)
# decorated_function()

######### ADVANCED PYTHON DECORATORS #########
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


user = User("Ozod")
user.is_logged_in = True
create_blog_post(user)