from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
x_position = [0, -20, -40]

for turtle_index in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.goto(x=x_position[turtle_index], y=0)











screen.exitonclick()