from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_in_on = True

while game_in_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_in_on = False
        score.game_over()

    for turtle in snake.turtles:
        if turtle == snake.head:
            pass
        elif snake.head.distance(turtle) < 10:
            game_in_on = False
            score.game_over()


screen.exitonclick()