import turtle as t
import random

tim = t.Turtle()


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fast")
t.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_c = (red, green, blue)
    return random_c


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
