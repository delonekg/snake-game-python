import turtle

# VALUES
X_COORDINATES = [0, -20, -40]
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # Snake Object Constructor
    def __init__(self):

        self.all_parts = []
        self.create_snake()
        self.head = self.all_parts[0]

    # Create a Snake
    def create_snake(self):
        for coordinate in X_COORDINATES:
            snake_part = turtle.Turtle(shape="square")
            snake_part.color("green")
            snake_part.penup()
            snake_part.goto(coordinate, 0)
            self.all_parts.append(snake_part)

    # Create an individual part of the snake
    def create_part(self, position):
        snake_part = turtle.Turtle(shape="square")
        snake_part.color("green")
        snake_part.penup()
        snake_part.goto(position)
        self.all_parts.append(snake_part)

    # Add new body part to snake
    def extend(self):
        self.create_part(self.all_parts[-1].position())

    # Resets the snake

    def reset(self):
        for part in self.all_parts:
            part.hideturtle()
        self.all_parts.clear()
        self.create_snake()
        self.head = self.all_parts[0]

    # Move the snake
    def move(self):
        for part_num in range(len(self.all_parts) - 1, 0, -1):
            self.all_parts[part_num].goto(self.all_parts[part_num - 1].pos())
        self.head.forward(SPEED)

    # Go up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Go down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Turn left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Turn right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
