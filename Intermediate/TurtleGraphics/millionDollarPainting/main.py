import turtle as t
from turtle import Screen
import math
import random

mpabbe = t.Turtle()
my_screen = Screen()
t.colormode(255)


## Walking left and forward (Triangle)
# mpabbe.forward(100)
# mpabbe.left(120)
# mpabbe.forward(100)
# mpabbe.left(120)
# mpabbe.forward(100)

## Square with right and backward
# mpabbe.up() 
# mpabbe.backward(100)
# mpabbe.right(90)
# mpabbe.backward(100)
# mpabbe.right(90)
# mpabbe.backward(100)
# mpabbe.right(90)
# mpabbe.backward(100)
# mpabbe.down()


## Chaning color, shape and width
# mpabbe.color("green")

# mpabbe.backward(100)
# mpabbe.right(90)
# mpabbe.backward(100)
# mpabbe.right(90)
# mpabbe.backward(100)
# mpabbe.right(90)
# mpabbe.backward(100)

# my_screen.clearscreen()


## create a visual
# mpabbe.shape("turtle")
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         mpabbe.color(c)
#         mpabbe.forward(steps)
#         mpabbe.right(30)

##### Drawing a dashed line #####
# for _ in range(15):
#     mpabbe.down()
#     mpabbe.forward(10)
#     mpabbe.up()
#     mpabbe.forward(10)

###### Drawing a different shape ######
colors = [
    "red",
    "dodger blue",
    "lime green",
    "orange",
    "violet",
    "gold",
    "deep pink",
    "turquoise"
]

## drawing a triangle
# for shape in range(3, 11):
#     mpabbe.color(colors[shape - 3])
#     for _ in range(shape):
#         mpabbe.forward(100)
#         mpabbe.right(360 / shape)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

### Drawing a random walk
# directions = [0, 90, 180, 270]
# mpabbe.pensize(20)
# mpabbe.speed("fastest")

# for _ in range(200):
#     mpabbe.color(random_color())
#     mpabbe.forward(30)
#     mpabbe.setheading(random.choice(directions))


######### Drawing a random spirograph #########
# def draw_spirograph(size_of_gap):
#     for _ in range(360 // size_of_gap):
#         mpabbe.color(random_color())
#         mpabbe.circle(100)
#         mpabbe.setheading(mpabbe.heading() + size_of_gap)

# mpabbe.speed("fastest")
# draw_spirograph(5)





my_screen.exitonclick()

