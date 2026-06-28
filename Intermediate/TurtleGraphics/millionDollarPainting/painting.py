# import turtle as t
# from turtle import Screen
# import random

# # import colorgram
# # ## Extracting colors 
# # all_colors = colorgram.extract("image.avif", 15)
# # rgb_colors = []
# # for color in all_colors:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     rgb_colors.append((r, g, b))

# turtle = t.Turtle()
# my_screen = Screen()
# t.colormode(255)

# colors = [(211, 161, 102), (158, 70, 45), (58, 102, 134), (222, 202, 137), (165, 151, 43), (137, 32, 21), (205, 90, 66), (44, 122, 85), (131, 162, 185), (146, 179, 147), (91, 73, 74)]


# ### Setting starting position
# def starting_position():
#     turtle.penup()
#     turtle.setpos(-240, -240)
#     turtle.pendown()

# ### draw a dot and walk
# def walking_ten_steps():
#     for _ in range(11):
#         turtle.dot(25, random.choice(colors))
#         turtle.penup()
#         turtle.forward(50)
#         turtle.pendown()
        

# def draw_everything():
#     for turn in range(1, 12):
#         walking_ten_steps()
#         turtle.penup()
#         turtle.setpos(-240, -240 + 50*turn)
    

# ### Drawing a dot
# ### Stopping
# turtle.speed(10)
# turtle.hideturtle()
# starting_position()
# draw_everything()



# my_screen.exitonclick()
