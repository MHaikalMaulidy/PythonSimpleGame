import random
import turtle as t

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:
    def __init__(self):
        self.kar = []
        self.waktu = 0.2
        self.movement = 0.2

    def make(self):
        mobil = t.Turtle('square')
        mobil.color(random.choice(COLORS))
        mobil.penup()
        mobil.shapesize(1, 2)
        mobil.goto(280, random.randint(-200, 250))
        self.kar.append(mobil)

    def move(self):
        for i in self.kar:
            i.goto(i.xcor()-20, i.ycor())

    def level_up(self):
        self.movement *= 0.9

    def reset(self):
        self.movement = 0.1
      #  self.x_move *= -1
