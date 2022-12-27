from turtle import Screen
import time
from snake import Snake
from food import Food
import random
from scorecard import Scorecard

# create a GUI for  snake gaming

screen = Screen()
screen.bgcolor("black")
screen.setup(height=400, width=400)
screen.title("Snake Game")


# create the simple snake

# t1 = Turtle()
# t1.shape("square")
# t1.color("white")
# t2 = Turtle()
# t2.shape("square")
# t2.color("white")
# t2.penup()
# t2.goto(x=-20, y=0)
# t3 = Turtle()
# t3.shape("square")
# t3.color("white")
# t3.penup()
# t3.goto(x=-40, y=0)



screen.tracer(0)

s = Snake()

screen.update()

# control the snake

screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")

# display food

l = Food()

# display scoreboard

t = Scorecard(0)


# simulate the snake

isgameon = True
scoreboard = 0
while isgameon:
    screen.update()
    time.sleep(0.1)
    s.forward()



# detecting food

    if (s.head.distance(l.food.position()))<25:
        l.food.goto(random.randint(-180,180), random.randint(-180,180))
        scoreboard += 5

# update scoreboard

    t.update(scoreboard)

    # method - 1
    # for i in segment:
    #     i.forward(20)

    # method -2 : making last segment to follow second -last so that on turn it follows properly as we needed

    if s.head.xcor() == 200 :
        isgameon = False
    elif s.head.xcor() == -200:
        isgameon = False
    elif s.head.ycor() == 200:
        isgameon = False
    elif s.head.ycor() == -200:
        isgameon = False
    else:
        pass





print(scoreboard)



screen.exitonclick()