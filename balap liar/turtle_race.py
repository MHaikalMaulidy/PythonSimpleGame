import random
import turtle as t

warna = ['red', 'blue', 'cyan', 'green', 'black']
screen = t.Screen()
screen.setup(1200, 700)
bet = screen.textinput('make your bet'.title(
), 'Which turtle will win the race red,blue,cyan,black or green?').lower()
user_bet = False
posisi = 200
pembalap = []
for i in range(0, 5):
    kura = t.Turtle()
    kura.speed('fastest')
    kura.shape('turtle')
    kura.color(warna[i])
    kura.penup()
    kura.goto(-590, posisi)
    kura.pendown()
    pembalap.append(kura)
    posisi -= 100


if bet:
    user_bet = True

while user_bet:
    for i in pembalap:
        i.forward(random.randint(10, 20))
        if i.xcor() > 590:
            menang = i.color()[0]
            user_bet = False
            break
loser = []
p = 1000
for i in pembalap:
    if i.xcor() < p:
        loser = i
        p = i.xcor()
if bet == menang:
    print('YOU WIN!!')
else:
    print(f'You lose, {menang} is the winning turtle')
print(f'And The LOSERS IS {loser.color()[0]}!!')

t.exitonclick()
