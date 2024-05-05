from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(0.7, 5)
        self.penup()
        self.goto((0, -280))
        self.paddle_speed = 0

    def move_left(self):
        self.paddle_speed = -7

    def move_right(self):
        self.paddle_speed = 7

    def stop_paddle(self):
        self.paddle_speed = 0

    def paddle_reset(self):
        self.goto((0, -280))
