
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from bonus import Bonus
import time
import random


FRAME_RATE = 90  # Frames per second
TIME_FOR_1_FRAME = 1 / FRAME_RATE  # Seconds

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Breakdown Game")
screen.tracer(0)


paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()
bonus = Bonus()
bricks.create_bricks()

screen.listen()


def start_game():
    global game_on
    game_on = not game_on
    return game_on


screen.onkeypress(start_game, "space")

screen.onkeypress(fun=paddle.move_left, key="Left")
screen.onkeypress(fun=paddle.move_right, key="Right")
screen.onkeyrelease(paddle.stop_paddle, "Left")
screen.onkeyrelease(paddle.stop_paddle, "Right")

screen.onkeypress(fun=paddle.move_left, key="a")
screen.onkeypress(fun=paddle.move_right, key="d")
screen.onkeyrelease(paddle.stop_paddle, "a")
screen.onkeyrelease(paddle.stop_paddle, "d")

bounce_mode = True
game_on = False
bricks_destroyed = 0


def ball_with_brick_collision():
    global bounce_mode, game_on, bricks_destroyed
    # List to store all bricks touched by the ball
    bricks_hit = []
    # Calculating the boundary points of the ball
    ball_left = ball.xcor() - 10
    ball_right = ball.xcor() + 10
    ball_top = ball.ycor() + 10
    ball_bottom = ball.ycor() - 10

    # Iterating through all bricks to find collisions
    for brick in bricks.bricks_list:
        brick_height = brick.shapesize()[0] * 10
        brick_width = brick.shapesize()[1] * 10

        brick_left = brick.xcor() - int(brick_width)
        brick_right = brick.xcor() + int(brick_width)
        brick_top = brick.ycor() + int(brick_height)
        brick_bottom = brick.ycor() - int(brick_height)

        horizontal = False

        # Checking for horizontal collision
        x_collision = brick_left < ball_right and brick_right > ball_left
        y_collision = brick_bottom < ball_top and brick_top > ball_bottom

        if x_collision and y_collision:
            horizontal = True

        if horizontal and len(bricks_hit) <= 2:
            bricks_destroyed += 1
            num = random.randint(9, 12)
            print(num)
            if num == 9 or num == 11:
                bonus.generate_bonus(brick.xcor(), brick.ycor(), "red")
            elif num == 5 or num == 7:
                bonus.generate_bonus(brick.xcor(), brick.ycor(), "green")
            elif num == 10:
                bonus.generate_bonus(brick.xcor(), brick.ycor(), "yellow")
            elif num == 15:
                bonus.generate_bonus(brick.xcor(), brick.ycor(), "blue")

            scoreboard.increase_score()
            bricks_hit.append(brick)

            # Destroy all bricks hit by the ball
            for brick_hit in bricks_hit:
                if bounce_mode:
                    ball.bounce()
                    brick_hit.goto(500, 500)  # Destroy the brick
                elif bounce_mode and len(bricks_hit) == 2:
                    ball.bounce()
                    brick_hit.goto(500, 500)  # Destroy the brick
                else:
                    brick_hit.goto(500, 500)  # Destroy the brick


game_timer = time.time()
screen.update()


while True:
    if game_on:
        timer_this_frame = time.time()
        time_for_this_frame = time.time() - timer_this_frame
        if time_for_this_frame < TIME_FOR_1_FRAME:
            time.sleep(TIME_FOR_1_FRAME - time_for_this_frame)

        screen.update()

        # Move ball
        ball.move_ball()
        bonus.move_bonus()

        if ball.ycor() < -269 and ball.xcor() >= paddle.xcor() and  ball.xcor() <= paddle.xcor() + 55:
            ball.x_move = 0.35
            if ball.ycor() < -269 and ball.xcor() >= paddle.xcor() and  ball.xcor() <= paddle.xcor() + 40:
                ball.x_move = 0.3
                if ball.ycor() < -269 and ball.xcor() >= paddle.xcor() and ball.xcor() <= paddle.xcor() + 30:
                    ball.x_move = 0.25
                    if ball.ycor() < -269 and ball.xcor() >= paddle.xcor() and ball.xcor() <= paddle.xcor() + 20:
                        ball.x_move = 0.2
                        if ball.ycor() < -269 and ball.xcor() >= paddle.xcor() and ball.xcor() <= paddle.xcor() + 10:
                            ball.x_move = 0.1
                            if ball.ycor() < -269 and ball.xcor() >= paddle.xcor() and ball.xcor() <= paddle.xcor() + 5:
                                ball.x_move = 0
            ball.bounce()
        if ball.ycor() < -269 and ball.xcor() < paddle.xcor() and  ball.xcor() > paddle.xcor() - 55:
            ball.x_move = -0.35
            if ball.ycor() < -269 and ball.xcor() < paddle.xcor() and ball.xcor() > paddle.xcor() - 40:
                ball.x_move = -0.3
                if ball.ycor() < -269 and ball.xcor() < paddle.xcor() and ball.xcor() > paddle.xcor() - 30:
                    ball.x_move = -0.25
                    if ball.ycor() < -269 and ball.xcor() < paddle.xcor() and ball.xcor() > paddle.xcor() - 20:
                        ball.x_move = -0.2
                        if ball.ycor() < -269 and ball.xcor() < paddle.xcor() and ball.xcor() > paddle.xcor() - 10:
                            ball.x_move = -0.1
                            if ball.ycor() < -269 and ball.xcor() < paddle.xcor() and ball.xcor() > paddle.xcor() - 5:
                                ball.x_move = 0
            ball.bounce()

        # Bounce from walls
        if ball.xcor() < -390 or ball.xcor() > 380:
            ball.bounce_from_wall()
        if ball.ycor() > 290:
            ball.bounce()

        # Move paddle
        paddle.setx(paddle.xcor() + paddle.paddle_speed)

        # Check borders for paddle
        if paddle.xcor() > 340:
            paddle.setx(340)
            paddle.paddle_speed = 0

        if paddle.xcor() < -345:
            paddle.setx(-345)
            paddle.paddle_speed = 0

        ball_with_brick_collision()

        if len(bonus.bonus_list) > 0:
            if bonus.bonus_list[0].ycor() < -270:
                if (bonus.bonus_list[0].xcor() >= paddle.xcor() and bonus.bonus_list[0].xcor() <= paddle.xcor() + 55) or \
                   (bonus.bonus_list[0].xcor() < paddle.xcor() and bonus.bonus_list[0].xcor() > paddle.xcor() - 55):
                    if bonus.catch_bonus() == "red":
                        ball.standard_ball_speed = ball.ball_speed * 1.5
                    elif bonus.catch_bonus() == "green":
                        ball.standard_ball_speed = ball.ball_speed * 0.7
                    elif bonus.catch_bonus() == "yellow":
                        bounce_mode = False
                    elif bonus.catch_bonus() == "blue":
                        bounce_mode = True

        # Game over
        if ball.ycor() < -280:
            ball.reset_ball()
            bounce_mode = True
            game_on = False
            paddle.goto((0, -280))
            scoreboard.decrease_lives()
            if scoreboard.lives < 0:
                scoreboard.game_over()
                game_on = False

    else:
        screen.update()
        time.sleep(0.1)

screen.exitonclick()
