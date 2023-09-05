import time
import turtle as t

from ball import Ball
from move import Move
from score import Scoreboard

screen = t.Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
player1 = Move(350, 0)
player2 = Move(-350, 0)
bola = Ball()
screen.listen()
screen.onkey(player1.go_up, 'Up')
screen.onkey(player1.go_down, 'Down')
screen.onkey(player2.go_up, 'w')
screen.onkey(player2.go_down, 's')
score = Scoreboard()
game = True
bola.setheading(45)
while game:
    screen.update()
    time.sleep(bola.movement)
    bola.move()

    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.bounce_y()

    # if bola.xcor() > 320:
     #   player1.goto(x=player1.xcor(), y=bola.ycor())

    if bola.distance(player1) < 150 and bola.xcor() > 320 or bola.distance(player2) < 150 and bola.xcor() < -320:
        bola.bounce_x()

    elif bola.xcor() < -380:
        bola.reset()
        score.nambah_skor1()

    elif bola.xcor() > 380:
        bola.reset()
        score.nambah_skor2()


screen.exitonclick()
