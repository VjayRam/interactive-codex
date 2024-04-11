from turtle import *
from random import randint

# set the background color
bgcolor('black')

# define the turtle
t = Turtle()
t.speed(0)
t.hideturtle()

# set the pen color
t.pencolor('red')

# define the mouse event
def mousemove(x,y):
    t.goto(x,y)
    t.dot(randint(1,20))

# listen for mouse events
listen()
onscreenclick(mousemove)

mainloop()