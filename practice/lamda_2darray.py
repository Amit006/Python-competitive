rows = 3
cols = 2
a = [ ([1] * cols) for row in range(rows)]
print("This IS ok.  At first:")
print("   a =", a)

a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a =", a)
a[1][0] = 60
print("a =",a)
a[2][0] = 34
print("a = ",a)



