
def prime(n):
    for num in range(2,n+1):
        while n > 1:
            for i in range(2,num):
                if (num % i != 0):
                    print("prime number",num)

prime(10)
