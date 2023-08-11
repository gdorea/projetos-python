from turtle import Turtle, Screen

tim = Turtle()
for steps in range(25):
    for c in ('black', 'white'):
        tim.color(c)
        tim.forward(5)



screen = Screen()
screen.exitonclick()