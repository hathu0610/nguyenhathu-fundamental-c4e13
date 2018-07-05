from turtle import * 

shape("turtle")
color("blue")
speed(-1)

for i in range (24):
    for j in range (4):
        forward (100)
        right (90)
    right(360/24)



mainloop()