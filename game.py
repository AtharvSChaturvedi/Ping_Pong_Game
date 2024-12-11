from turtle import Screen
from paddlebar import Paddle_Bar
from ball import Ball
from scorecard import Score
import time

screen=Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

r_paddle_bar=Paddle_Bar((350,0))
l_paddle_bar=Paddle_Bar((-350,0))

the_ball=Ball()

scoreboard=Score()
l_score=0
r_score=0

screen.listen()
screen.onkeypress(r_paddle_bar.go_up, "Up")
screen.onkeypress(r_paddle_bar.go_down, "Down")
screen.onkeypress(l_paddle_bar.go_up, "w")
screen.onkeypress(l_paddle_bar.go_down, "s")

game=True
while game:
    time.sleep(the_ball.change_speed)
    screen.update()
    the_ball.move()

    #collision with wall
    if the_ball.ycor()>280 or the_ball.ycor()< -280:
        the_ball.y_bounce()

    #collision with right paddle
    if the_ball.distance(r_paddle_bar)<50 and the_ball.xcor()>320:
        the_ball.x_bounce()
    
    #collision with left paddle
    if the_ball.distance(l_paddle_bar)<50 and the_ball.xcor()<-320:
        the_ball.x_bounce()

    #right paddle misses it
    if the_ball.xcor()>400:
        the_ball.reset_position()
        scoreboard.l_point()
        l_score+=1

    #left paddle misses it
    if the_ball.xcor()<-400:
        the_ball.reset_position()
        scoreboard.r_point()
        r_score+=1

    if l_score==5:
        scoreboard.winner_l()
        game=False
    
    if r_score==5:
        scoreboard.winner_r()
        game=False
        
        
screen.exitonclick()
