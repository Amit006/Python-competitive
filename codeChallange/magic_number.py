
prime_lst = []
magic_lst = []

#prime Number :

def prime(n):
    for num in range(2,n+1):
        print("value of num",num)
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0 :
                    print("num:{0} % {1} == 0 ".format(num,i))
                    break
            else:
                print("prime number========",num)
                prime_lst.append(num)
                print(prime_lst)


def magic(l,r):
    for i in range(l,r+1):
        print("value of l:{} and r:{} :".format(l,r))
        for x in prime_lst:
            k = i % x
            print("i:{} % x{} == {}" .format(i,x,k))
            if (i % x) == 0:
                magic_lst.append(i)
                print("append value:",i)
                break


def display():
    for i in magic_lst:
        print("the magic number is:{}".format(i))
    
    print("total magic number is:{}".format(len(magic_lst)))

def flash_f8():
    global prime_lst,magic_lst
    if prime_lst:
        prime_lst = []
    if magic_lst:
        magic_lst = []

if __name__=='__main__':
    take_input = int(input("enter how many times"))
    for i in range(0,take_input):
        n = int(input("n value"))
        l = int(input("l value"))
        r = int(input("r value"))
        flash_f8()
        prime(n)
        magic(l,r)
        display()
        flash_f8() 
    