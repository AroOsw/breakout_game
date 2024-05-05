from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.shapesize(1, 1)
        self.goto(0, 0)
        self.x_move = 0
        self.y_move = 1
        self.ball_speed = 5
        self.standard_ball_speed = 5
        self.ball_width = self.shapesize()[0] * 10
        self.ball_height = self.shapesize()[1] * 10
        self.lvl = 0

    def move_ball(self):
        self.sety(self.ycor() - (self.y_move * self.ball_speed))
        self.setx(self.xcor() - (self.x_move * self.ball_speed))

    def bounce(self):
        self.y_move *= -1

    def bounce_from_wall(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move = 0
        self.y_move = 1
        self.ball_speed = self.standard_ball_speed
        self.move_ball()

    def increase_ball_speed(self):
        self.ball_speed += 1
        self.standard_ball_speed += 1

