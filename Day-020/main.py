from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ssssnake")
screen.tracer(0)

snake = Snake()
game_on=True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    screen.update()
    snake.move()

screen.exitonclick()
