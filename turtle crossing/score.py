import turtle as t

FONT = ("Courier", 24, "normal")


class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(-200, 200)
        self.write(f'LEVEL: {self.level}', False, 'center', FONT)

    def tambah(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER! ', False, 'center', FONT)


""" def ulang(self):
        self.level = 1
        self.clear()
        self.update()"""
