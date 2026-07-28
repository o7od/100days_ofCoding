from flask import Flask
import random

LOWER_GIF = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWI2bG1jZnN0dWE1cGR6ZGxrMzhuanV5MHNqcDVjdHRzanZlZjk5eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ZXBTXowuDiFbkiigKl/giphy.gif"
HIGHER_GIF = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ25nZWZub3M3cWtoMTM1cXV3eHB5b3phNjhsenplcGN5dmJvNHo4ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/nj7Liv1rNeplJ9YIYH/giphy.gif"
FOUND_ME_GIF = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2ZvOHE0eDMxMGJnY296a2E3ZXBobmkxdjR5dmV4YmIwczJrdzYxZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/JKcneNkriqxQbE8e49/giphy.gif"
GUESS_GIF = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnFnMWwwMmh5NG1jdDJ3amIwdGZlcTVsa2owenhzNzFycDdhdzNrbCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/YmQLj2KxaNz58g7Ofg/giphy.gif"

app = Flask(__name__)
true_value = random.randint(0, 9)
print(true_value)

# def check_guess(function):
#     def wrapper(*args):
#         if true_value > args[0]:


@app.route("/")
def guess_number():
    return "<h1 style='text-align: left'> Guess a number between 0 and 9 </h1>" \
    f"<img src='{GUESS_GIF}' width=500>"


@app.route("/<user_guess>")
def check_user_guess(user_guess):
    if int(user_guess) > true_value:
        return f"<img src='{HIGHER_GIF}' width=500>"
    elif int(user_guess) < true_value:
        return f"<img src='{LOWER_GIF}' width=500>"
    else:
        return f"<img src='{FOUND_ME_GIF}' width=500>"


if __name__ == "__main__":
    app.run(debug=True)