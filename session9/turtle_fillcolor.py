from turtle import *
color = ["red", "blue", "brown", "yellow", "grey"]
for i in range(5):
    fillcolor(color[i])
    begin_fill()
    for n in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    end_fill()
    forward(100)
mainloop()
