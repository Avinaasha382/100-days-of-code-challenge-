from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.title("PingPong")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
scoreboard = Scoreboard()

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()





screen.onkey(key = "w", fun = left_paddle.up)
screen.onkey(key="s",fun = left_paddle.down)
screen.onkey(key = "Up", fun = right_paddle.up)
screen.onkey(key="Down",fun = right_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.curr_speed)

    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()

    if (ball.distance(right_paddle)<50 and ball.xcor()>320) or (ball.distance(left_paddle)<50 and ball.xcor()<-320):
        ball.bounce_x()
        ball.curr_speed* 0.1



    if ball.xcor()>=380:
        ball.reset_ball()
        scoreboard.increase_leftscore()

    if ball.xcor()<=-380:
        ball.reset_ball()
        scoreboard.increase_rightscore()



screen.mainloop()