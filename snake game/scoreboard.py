import turtle as t

aligment = 'center'
font = ('Courier', 18, 'normal')
move = False


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updet()

    def updet(self):
        self.write(f'SCORE: {self.score}', move,
                   aligment, font)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(
            f'     GAME OVER!!\nYour Final Score is: {self.score}', move, aligment, font)

    def nambah_skor(self):
        self.score += 1
        self.clear()
        self.updet()
