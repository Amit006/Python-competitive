def make_incement(n):
    return lambda x:x+n

f=make_incement(42)
print(f)
print(f(0))
print(f(1))
print(f(10))
print(f(23))
