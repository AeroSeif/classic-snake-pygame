from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Slitherin Serpent 🐍")
screen.tracer(0)

score = ScoreBoard()
bait = Food()
snake = Snake()
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Adds a 0.1-minute delay after each segment moves.
    # So each segment moves, the screen updates, and then it sleeps for a second before the next time it happens
    snake.move()
    # Detect collision with food.
    if snake.head.distance(bait) < 20:
        bait.refresh()
        snake.extend()
        score.update()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    # Detect collision with tail. If head collides with any segment in tail, trigger "GAME OVER".
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
