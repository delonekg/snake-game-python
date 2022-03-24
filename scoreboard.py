from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align="center", font=("Courier", 30, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                self.high_score = self.score
                file.write(str(self.high_score))
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", align="center", font=("Courier", 30, "normal"))
    #     self.goto(0, -40)
    #     self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))

    def increment_score(self):
        self.score += 1
        self.update()
