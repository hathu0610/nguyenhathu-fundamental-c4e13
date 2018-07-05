from turtle import * 


shape("turtle")
color("blue")
speed(-1)

size = 5

for i in range (50):
    for j in range(4):
        forward(size)
        left(90)
        
    size = size + 4
    left(10)

mainloop()