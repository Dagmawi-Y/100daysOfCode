from turtle import Turtle, Screen

tur = Turtle()
scr = Screen()

tur.speed(2)

for _ in range(4):
    tur.forward(10)
    tur.penup()
    tur.forward(10)
    tur.pendown()

scr.exitonclick()
