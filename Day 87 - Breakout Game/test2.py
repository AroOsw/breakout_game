from turtle import Turtle, Screen


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("purple")
screen.title("Breakdown Game")
screen.tracer(0)


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.colors = ["white", "gray", "blue", "green", "yellow", "orange", "red", "brown"]
        self.x = -368
        self.y = 120
        self.bricks_list = []
        self.hideturtle()
        self.brick_width = self.shapesize()[0] * 10
        self.brick_height = self.shapesize()[1] * 10
        # self.y = y
        # self.x = x
        # self.shape("square")
        # self.color(self.colors[0])
        # self.shapesize(0.7, 2.6)
        # self.penup()
        # self.goto(self.x, self.y)

    def create_bricks(self):
        for i in range(8):
            for _ in range(14):
                new_brick = Turtle("square")
                new_brick.color(self.colors[i])
                new_brick.shapesize(0.7, 2.6)
                new_brick.penup()
                new_brick.goto(self.x, self.y)
                self.bricks_list.append(new_brick)
                self.x += 56
            self.x = -368
            self.y = self.y + 18


bricks = Bricks()
bricks.create_bricks()

game_on = True
while game_on:
    screen.update()


    for brick in bricks.bricks_list[:1]:
        brick.reset()
        brick.hideturtle()

screen.exitonclick()