import turtle
setround =8
for i in range(setround):
   turtle.forward(100)
   turtle.color("blue")
   turtle.right(100)
   turtle.right(200)
   turtle.color("orange")
   turtle.forward(100)
   if (setround == 3):
     turtle.color("yellow")
     turtle.forward(300/100)
     turtle.right(100)
     turtle.color("orange")
   for i in range(setround):
     turtle.forward(800)
     turtle.right(145)
     for i in range(setround):
       turtle.color("red")
       turtle.forward(180)
       turtle.right(100)
       turtle.color("orange")








