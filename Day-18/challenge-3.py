from turtle import Turtle, Screen

tim = Turtle()
tim.speed(2)


def draw_shape(num_of_shapes):
    for _ in range(num_of_shapes):
        tim.right(360 / num_of_shapes)
        tim.forward(90)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
