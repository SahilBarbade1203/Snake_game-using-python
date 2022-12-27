from turtle import Turtle

class Snake:

     def __init__(self):
         self.segment = []
         start_position = [(0, 0), (-20, 0), (-40, 0),(-60,0),(-80,0),(-100,0),(-120,0)]
         for items in start_position:
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.goto(items)
            (self.segment).append(t)
         self.head = self.segment[0]

     def forward(self):
         for i in range(len(self.segment) - 1, 0, -1):
             x = (self.segment[i - 1]).xcor()
             y = (self.segment[i - 1]).ycor()
             (self.segment[i]).goto(x, y)
         (self.segment[0]).forward(20)


     def up(self):
         if self.segment[0].heading() != 270:
             (self.segment[0]).setheading(90)
         else:
             pass

     def down(self):
         if self.segment[0].heading() != 90:
             (self.segment[0]).setheading(270)
         else:
             pass


     def left(self):
         if self.segment[0].heading() != 0:
             (self.segment[0]).setheading(180)
         else:
             pass



     def right(self):
         if self.segment[0].heading() != 180:
             (self.segment[0]).setheading(0)
         else:
             pass
