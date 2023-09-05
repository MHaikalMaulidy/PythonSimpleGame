import turtle as t

font = ('Courier', 58, 'normal')
move = False


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.updet1()
        self.updet2()

    def updet1(self):
        self.goto(100, 200)
        self.write(f'{self.score1}', move,
                   'right', font)

    def updet2(self):
        self.goto(-100, 200)
        self.write(f'{self.score2}', move,
                   'left', font)

    def nambah_skor1(self):
        self.score1 += 1
        self.clear()
        self.updet1()
        self.updet2()

    def nambah_skor2(self):
        self.score2 += 1
        self.clear()
        self.updet1()
        self.updet2()
