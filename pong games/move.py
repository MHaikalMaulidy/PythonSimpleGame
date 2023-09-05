import turtle as t


class Move(t.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(x=x, y=y)

    def go_up(self):
        new_y = self.ycor()+40
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor()-40
        self.goto(x=self.xcor(), y=new_y)
