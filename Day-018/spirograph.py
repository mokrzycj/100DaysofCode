from turtle import Turtle, Screen
# from random_walk import another_random_color
import random
screen=Screen()

timmy = Turtle()
timmy.speed("fastest")

def another_random_color():
    screen.colormode(255)
    r=random.randint(0,255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    # color_str = "#{:02X}{:02X}{:02X}".format(r, g, b)
    # color_str = f"({r}, {g}, {b})"
    color_str = (r, g, b)

    # print(color_str)
    return color_str


for i in range(0, 360, 2):
    timmy.pencolor(another_random_color())
    timmy.setheading(i)
    timmy.circle(150)






screen.exitonclick()
