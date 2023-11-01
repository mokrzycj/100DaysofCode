from turtle import Turtle, Screen
import random
screen=Screen()

timmy = Turtle()

def random_color():
    import secrets
    random_color = secrets.token_hex(3)
    random_color = "#" + random_color
    return random_color


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

def random_walk(steps):
    for _ in range(steps):
        # timmy.pencolor(random_color())

        timmy.color(another_random_color())
        timmy.pensize(15)
        timmy.speed('fast')

        timmy.forward(30)
        timmy.setheading(random.choice([0, 90, 180, 270]))


random_walk(200)




screen.exitonclick()