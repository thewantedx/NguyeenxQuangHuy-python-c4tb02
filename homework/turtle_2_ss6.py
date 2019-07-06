from turtle import *
color("red")
n=0
speed(-1)
while True:
    for i in range(10):
        for i in range(4):
            forward(n)
            left(90)
            n+=1
            if n<10:break
        left(10)
        
mainloop()