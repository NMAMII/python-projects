from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.ypos = 1
        self.xpos = 1
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.xpos
        new_y = self.ycor() + self.ypos
        self.goto(new_x,new_y)

    def bounce(self):
        self.ypos *= -1
        self.move_speed *= 0.9

    def bounce_paddle(self):
        self.xpos *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.01
        self.ypos *= -1
        self.xpos *= -1

