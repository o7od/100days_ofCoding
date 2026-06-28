import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=900, height=650)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)

# --- Draw stars slowly ---
for _ in range(150):
    x = random.randint(-450, 450)
    y = random.randint(-325, 325)
    size = random.uniform(1, 3)
    t.goto(x, y)
    t.dot(size, "white")
    screen.update()
    time.sleep(0.03)  # pause between each star

# --- Short pause before text appears ---
time.sleep(0.8)

# --- Glow layers appear one by one ---
glow_colors = ["#3a0033", "#7a006a", "#cc00aa", "#ff55dd", "white"]
sizes =        [105,       90,        78,        68,        60     ]

for color, size in zip(glow_colors, sizes):
    t.color(color)
    t.goto(0, -size // 2)
    t.write("I Miss You", align="center", font=("Georgia", size, "bold italic"))
    screen.update()
    time.sleep(0.4)  # pause between each glow layer

# --- Final pause to admire ---
time.sleep(1)
turtle.done()