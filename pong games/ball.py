import turtle as t


class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('red')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setpos(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.movement = 0.1

    def move(self):
        new_X = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_X, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.movement *= 0.9

    def reset(self):
        self.home()
        self.movement = 0.1
        self.x_move *= -1
