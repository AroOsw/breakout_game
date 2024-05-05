from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.lives = 2
        self.lvl = 1
        self.color("white")
        self.teleport(0, 275)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        if self.lives < 0:
            self.write(f"Lives: {0} | Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"Lvl: {self.lvl} | Lives: {int(self.lives)} | Score: {self.score} | Press Space to start/pauze", align=ALIGNMENT, font=FONT)

    def decrease_lives(self):
        self.lives -= 1
        self.score -= 100
        self.update_scoreboard()

    def increase_lives(self):
        self.lives += 0.5
        self.update_scoreboard()

    def game_over(self):
        game_over = Turtle()
        game_over.goto(0, 0)
        game_over.color("white")
        game_over.write("Game Over", align="center", font=("Courier", 30, "normal"))


