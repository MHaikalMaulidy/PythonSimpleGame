import random
import time
import turtle as t

from car import Car
from mc import Mc
from score import Score

screen = t.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
mc = Mc()
car = Car()
score = Score()
screen.listen()
screen.onkey(mc.up, 'Up')
screen.onkey(mc.right, 'Right')
screen.onkey(mc.left, 'Left')
game = True
while game:
    screen.update()
    time.sleep(car.movement)
    if random.randint(1, 4) == 3:
        car.make()
    car.move()
    for i in car.kar:
        if mc.distance(i) < 20:
            score.game_over()
            # score.ulang()
            # mc.reset()
            game = False
            break

    if mc.ycor() > 280:
        score.tambah()
        mc.reset()
        car.level_up()


screen.exitonclick()
