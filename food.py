from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_position_x = random.randint(-290, 290)
        rand_position_y = random.randint(-290, 290)
        move = (rand_position_x, rand_position_y)
        self.goto(move)