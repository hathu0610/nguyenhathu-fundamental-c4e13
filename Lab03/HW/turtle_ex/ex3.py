from turtle import *

shape("turtle")
speed(-1)


def draw_square(length, colors):
    shape("turtle")
    speed(-1)
    color(colors)
    for i in range(4):
        forward(length)
        left(90)
    
    return

for i in range(30):
    draw_square(i*5, "red")
    left(17)
    penup()
    forward(i*2)
    pendown()

mainloop()

    