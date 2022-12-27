from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self, scorecard):
        super().__init__()
        self.score = scorecard
        self.color("white")
        self.penup()
        self.goto(0, 165)
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()


    def update(self, score):
        self.clear()
        self.write(f"Score = {score}", align="center", font=("Arial", 24, "normal"))
