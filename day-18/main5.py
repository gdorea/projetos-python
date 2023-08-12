import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

moves = [0, 90, 180, 270]

tim.shape("classic")
tim.pensize(15)
tim.speed("fastest")


for n in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(moves))

screen = t.Screen()
screen.exitonclick()