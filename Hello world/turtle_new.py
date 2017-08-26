import turtle

nbrsides = 20

for i in range(20):
  for steps in ["black", "blue", "green", "Yellow", "orange"]:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(720 - 30)
    for steps in ["black", "blue", "green", "Yellow", "orange","red", "brown"]:
      turtle.color(steps)
      turtle.forward(100)
      turtle.right(720 - 35)
j = 0
for i in range(20):
  for j in range(i-j, i):
    turtle.color("blue")
    turtle.forward(100)
    turtle.right(100)