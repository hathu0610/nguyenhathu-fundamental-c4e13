
from turtle import * 
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
shape("turtle")
speed(-1)

turtle_color = 0

for i in range(3,8):
    for j in range(i):
        forward(100)
        left(360/i)
        color(colors[turtle_color])
    turtle_color+=1

        
    


mainloop()