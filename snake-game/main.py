from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
x_position = [0, -20, -40]
turtles = []
screen.tracer(0)

for turtle_index in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=x_position[turtle_index], y=0)
    turtles.append(new_turtle)

game_in_on = True

while game_in_on:
    screen.update()
    time.sleep(0.1)

    for turtle_num in range(len(turtles) - 1, 0, -1):
        new_x = turtles[turtle_num - 1].xcor()
        new_y = turtles[turtle_num - 1].ycor()
        turtles[turtle_num].goto(new_x, new_y)
    turtles[0].forward(20)


screen.exitonclick()