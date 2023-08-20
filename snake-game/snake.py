from turtle import Turtle

X_POSITION = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self) -> None:
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for turtle_index in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=X_POSITION[turtle_index], y=0)
            self.turtles.append(new_turtle)

    def move(self):
        for turtle_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_num - 1].xcor()
            new_y = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
