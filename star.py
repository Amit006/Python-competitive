n=int(input("Enter the number:"))

for i in range(1,n+1):
    
    for s in range(i,n+1):
        print(" ",end="")

    for j in range(1,i*2):
        print("*",end="")

    print("\n")


import sys # Used for the sys.exit function
int_condition = 5
if int_condition < 6:
 sys.exit("int_condition must be >= 6 ")
else:
 print("int_condition was >= 6 - continuing")