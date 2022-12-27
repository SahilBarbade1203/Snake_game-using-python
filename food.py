from turtle import Turtle
import random

x = random.randint(-165,165)
y = random.randint(-165,165)


class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.color("white")
        self.food.turtlesize(0.5,0.5,1)
        self.food.color("blue")
        self.food.penup()
        self.food.goto(x,y)




