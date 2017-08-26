y=input("Enter number")

try:
    x = float(y)
    inverse = 1.0 / x
    print(inverse)
except ValueError:
    print("you should have either provide int or posative integer")
except ZeroDivisionError:
    print("divide by zero is not possiable")
finally:
    print("there may or may not have been error")
