from turtle import *
from random import *


def star():
    begin_fill()
    size = randint(20,50)
    for i in range(5):
        forward(size)
        left(144)

    end_fill()

speed(0)

color('dark blue')
begin_fill()
goto(-200,200)
for q in range(4):
    forward(400)
    right(90)
end_fill()
color('yellow')
for e in range(50):
    penup()
    goto(0,0)
    goto(randint(-150,150),randint(-150,150))
    pendown()
    star()

input()
