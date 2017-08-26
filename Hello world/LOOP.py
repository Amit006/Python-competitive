x = 2
while x <= 10:
    z = 5
    x += 1
    while z <= 10:
        print(z)
        z += 1

list1= [ 2,5,4]
list2= [10,11,15,16,19]
for i in list1:
    for j in list2:
        if j == 20:
            break
        else:
             j+=3
        print(i, '*', j, "multiplication number:",  j * i )
    print('out of the loop')
