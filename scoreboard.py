from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.project()

    def project(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_high:
                new_high.write(f"{self.high_score}")
        self.score = 0
        self.project()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER🐍", move=False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.project()
