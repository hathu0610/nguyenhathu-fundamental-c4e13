from turtle import * 
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
shape("turtle")
speed(-1)
turtle_color = 0
for i in range(5):
    color(colors[turtle_color])
    begin_fill()
    for j in range (2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    end_fill()
    forward(50)
    turtle_color+=1

mainloop()