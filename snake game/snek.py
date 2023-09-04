import turtle as t

snak = [(0, 0), (-20, 0), (-40, 0)]
cepet = 20
kanan = 0
atas = 90
kiri = 180
bawah = 270


class Snake:
    def __init__(self):
        self.uler = []
        self.make()
        self.head = self.uler[0]

    def make(self):
        for i in snak:
            self.nambah_panjang(i)

    def nambah_panjang(self, x):
        piton = t.Turtle('square')
        piton.penup()
        piton.color('white')
        piton.goto(x)
        self.uler.append(piton)

    def makan(self):
        self.nambah_panjang(self.uler[-1].position())

    def move(self):
        for i in reversed(self.uler):
            index_uler = self.uler.index(i)
            if index_uler == 0:
                break
            new_x = self.uler[index_uler-1].xcor()
            new_y = self.uler[index_uler-1].ycor()
            self.uler[index_uler].goto((new_x, new_y))
        self.head.forward(cepet)

    def kanan(self):
        if self.head.heading() != kiri:
            self.head.setheading(kanan)

    def atas(self):
        if self.head.heading() != bawah:
            self.head.setheading(atas)

    def kiri(self):
        if self.head.heading() != kanan:
            self.head.setheading(kiri)

    def bawah(self):
        if self.head.heading() != atas:
            self.head.setheading(bawah)
