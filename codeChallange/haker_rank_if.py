n = int(input())
if (n % 2 == 0):
    if n in range(2, 5+1):
        print("1st if ststement ")
        print("not weird")
    elif n in range(6, 20+1):
        print("2nd if statement")
        print("weird")
    elif (n > 20+1):
        print("3rd if statement")
        print("not weird")
else:
    print("last else statement")
    print("weird")







