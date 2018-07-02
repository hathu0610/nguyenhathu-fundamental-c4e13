from turtle import * 

shape("turtle")
speed(-1)


for i in range(3,7):
    if i % 2 == 1 :
       color("blue")

    else:
        color("red") 
    for j in range(i):
           forward(100)
           left(360/i)
       
   

mainloop()