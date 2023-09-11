import random
import time
import turtle as t

import pandas

skor = t.Turtle()
skor.hideturtle()
skor.penup()
skor.goto(-270, 250)
p = t.Turtle()
p.penup()
p.color('#ff03c8')
p.shape('circle')
p.shapesize(0.5, 0.5)
p.hideturtle()
p.goto(0, 270)
screen = t.Screen()
screen.title('ADA INDO COY!!!')
gambar = 'indonesia.gif'
screen.addshape(gambar)
t.shape(gambar)
data = pandas.read_csv('provinsi.csv')
score = 0
tempat = data.wilayah.to_list()
color = ['#ff03c8', '#ff0037', '#7b2eff', '#00d5ff', '#86d400']
jawaban = []
skor.write(f'{score}/8', False,
           'center', ('Courier', 40, 'bold'))
while score < 8:
    tebak = screen.textinput('Tebak Provinsi', 'JAWAB: ').title()
    if tebak == 'Jawa':
        tebak = 'Jawir'
    if tebak == 'Opm':
        tebak = 'Papua'
    if tebak == 'Ntb':
        tebak = 'NTB'
    if tebak == 'Ntt':
        tebak = 'NTT'
    if tebak in tempat and tebak not in jawaban:
        time.sleep(0.5)
        x_cor = data[data.wilayah == tebak].x[tempat.index(tebak)]
        y_cor = data[data.wilayah == tebak].y[tempat.index(tebak)]
        p.showturtle()
        p.color(random.choice(color))
        p.goto(x_cor, y_cor)
        p.write(tebak, move=False, align='center',
                font=('Arial', 20, 'bold'))
        score += 1
        jawaban.append(tebak)
        skor.clear()
        skor.write(f'{score}/8', False,
                   'center', ('Courier', 40, 'bold'))
    p.hideturtle()
    p.goto(0, 270)

skor.clear()
skor.goto(0, 0)

while 1 == 1:
    for i in color:
        skor.color(i)
        skor.write('YOU WIN!!!!', False,
                   'center', ('Courier', 70, 'bold'))
        time.sleep(1)
        skor.clear()

screen.exitonclick()
"""" def x(x, y):
    print(x, y)
t.onscreenclick(x)
t.mainloop()"""
