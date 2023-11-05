STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
DOWN = 270.0
UP = 90.0
LEFT = 180.0
RIGHT = 0.0

from turtle import Turtle
class Snake():
    from turtle import Turtle
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            tim = Turtle()
            tim.shape("square")
            tim.penup()
            tim.color("white")
            tim.goto(position)
            self.segments.append(tim)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            seg_pos = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(seg_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].ycor() + MOVE_DISTANCE != self.segments[1].ycor():
            self.head.setheading(UP)

    def down(self):
        if self.segments[0].ycor() - MOVE_DISTANCE != self.segments[1].ycor():
            self.head.setheading(DOWN)

    def left(self):
        if self.segments[0].xcor() - MOVE_DISTANCE != self.segments[1].xcor():
            self.head.setheading(LEFT)

    def right(self):
        if self.segments[0].xcor() + MOVE_DISTANCE != self.segments[1].xcor():
            self.head.setheading(RIGHT)

