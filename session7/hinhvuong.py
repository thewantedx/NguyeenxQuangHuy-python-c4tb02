n=int(input("nhap vao 1 so > 100:"))
from turtle import *
color("green")
speed(-1)
for i in range(4):
    forward(n)
    left(90)
print("hinh vuong voi canh la so ban nhap la:")
mainloop()