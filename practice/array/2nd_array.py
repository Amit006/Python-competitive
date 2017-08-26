# Create a variable-sized 2d list
rows = 3
cols = 2

a=[]
for row in range(rows):
    a += [[0]*cols]
    print("structure of a ",a)

print("This IS ok.  At first:")
print ("a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print(" a =", a)
