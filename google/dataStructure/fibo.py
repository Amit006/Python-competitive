#[1,1,2,3,5,8]

def fib(n):
    print("printing from fib1")
    a,b=0,1
    while b< n :
        print(b, end=" ")
        a,b=b,a+b
    print()


# fib(10)
#fibonachi with array 
array=[]
def fib2(n):
    print("printing from fib2")
    a,b=0,1
    while b < n:
        print(b, end=" ")
        array.append(b)
        a,b=b,a+b
    return array


# fib2(10)
# print("arraay[];",array
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    fib2(int(sys.argv[2]))
    #doing fun 
    print(sys.ps1)
    print(sys.ps2)

