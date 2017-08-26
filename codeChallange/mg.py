prime_lst = []
magic_lst = []
#prime Number :
def prime(n):
    for num in range(2,n+1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0 :
                    break
            else:
                prime_lst.append(num)
                

def magic(l,r):
    for i in range(l,r+1):
        for x in prime_lst:
            k = i % x
            if (i % x) == 0:
                magic_lst.append(i)
                break


def display():
    print (len(magic_lst))

def flash_f8():
    global prime_lst,magic_lst
    if prime_lst:
        prime_lst = []
    if magic_lst:
        magic_lst = []

if __name__=='__main__':
    take_input = int(input())
    for i in range(0,take_input):
        n ,l, r = map(int,(input().strip().split()))
        flash_f8()
        prime(n)
        magic(l,r)
        display()
        flash_f8() 
    