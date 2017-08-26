import turtle

set_round = 200
color_round = ['green', 'blue', 'black']
for i in range(1, 100):
    turtle.color(color_round[0])
    turtle.right(100)
    turtle.forward(100)
    turtle.right(150)
    for j in range(1, 200):
        turtle.color(color_round[1])
        turtle.right(100)
        turtle.forward(100)
        turtle.right(100)
        continue


