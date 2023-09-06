import turtle as t


class Mc(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('blue')
        self.goto(0, -280)
        self.setheading(90)

    def reset(self):
        self.goto(0, -280)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def left(self):
        self.goto(self.xcor()-20, self.ycor())

    def right(self):
        self.goto(self.xcor()+20, self.ycor())
