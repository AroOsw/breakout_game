from turtle import Turtle

class Bonus(Turtle):
    def __init__(self):
        super().__init__()
        # self.colors = ["white", "gray", "blue", "green"]
        self.x_move = 0
        self.y_move = 1
        self.bonus_speed = 2
        self.bonus_list = []
        self.hideturtle()
        self.penup()

    def generate_bonus(self, x, y, color):
        new_bonus = Turtle("turtle")
        new_bonus.color(color)
        new_bonus.shapesize(1, 1)
        new_bonus.penup()
        new_bonus.goto(x, y)
        new_bonus.setheading(90)
        self.bonus_list.append(new_bonus)

    def move_bonus(self):
        for bonus in self.bonus_list:
            bonus.sety(bonus.ycor() - (self.y_move * self.bonus_speed))
            if bonus.ycor() < -275:
                bonus.goto(500, 500)
                self.bonus_list.remove(bonus)

    def catch_bonus(self):
        if self.bonus_list[0].color() == ("green", "green"):
            return "green"
        elif self.bonus_list[0].color() == ("red", "red"):
            return "red"
        elif self.bonus_list[0].color() == ("yellow", "yellow"):
            return "yellow"
        elif self.bonus_list[0].color() == ("blue", "blue"):
            return "blue"
        elif self.bonus_list[0].color() == ("gray", "gray"):
            return "gray"
