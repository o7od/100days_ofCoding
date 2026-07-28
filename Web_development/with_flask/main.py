from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        result = function()
        return f"<b>{result}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        result = function()
        return f"<em>{result}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        result = function()
        return f"<u>{result}</u>"

    return wrapper


@app.route('/')
def say_hello():
    return "<h1 style='text-align: center'> Hello </h1>" \
    "<p>This is a paragraph</p>" \
    "<img src='https://www.laughingplace.com/uploads/media/2026/03/1080p-HD-Video-5.jpg' width=500>"



@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)

