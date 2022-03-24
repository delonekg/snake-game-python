import turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

game_on = True

# Setup screen
window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Classic Snake")
window.tracer(0)

# Create the snake
snake = Snake()

# Create the food
food = Food()

# Create the scoreboard
scoreboard = ScoreBoard()

# Listen for input
window.listen()
window.onkey(key="Up", fun=snake.up)
window.onkey(key="Down", fun=snake.down)
window.onkey(key="Left", fun=snake.left)
window.onkey(key="Right", fun=snake.right)

# Main game loop
while game_on:
    window.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.move_location()
        scoreboard.increment_score()
        snake.extend()

    # Detect collisions with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for part in snake.all_parts[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset()

window.exitonclick()
