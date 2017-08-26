from turtle import *
color('red','blue')
def draw():
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

for i in range(0,3):
    print(draw(), end=" ")

