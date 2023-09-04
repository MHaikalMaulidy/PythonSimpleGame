import random
import time
import turtle as t

import scoreboard
from food import Food
from snek import Snake

jalan = Snake()
food = Food()
screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Uler Piton')
screen.tracer(0)

screen.listen()
screen.onkey(jalan.atas, 'Up')
screen.onkey(jalan.bawah, 'Down')
screen.onkey(jalan.kanan, 'Right')
screen.onkey(jalan.kiri, 'Left')
game_on = True
scor = scoreboard.Scoreboard()
while game_on:
    screen.update()
    time.sleep(0.2)

    jalan.move()
    if jalan.head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        jalan.makan()
        scor.nambah_skor()

    if jalan.head.xcor() > 280 or jalan.head.xcor() < -280 or jalan.head.ycor() > 280 or jalan.head.ycor() < -280:
        game_on = False
        scor.game_over()

    for i in jalan.uler:
        if i == jalan.head:
            pass
        elif jalan.head.distance(i) < 10:
            game_on = False
            scor.game_over()
            break


screen.exitonclick()
