from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", True, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", True, align="center")
    def count(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()