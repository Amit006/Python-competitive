i= 5
def f(arg=i):
	print(arg)

i=6
f()
f(i)

def fun(a,l=[]):
        if(l is None):
                l.append(a)
                #return l
        else:
                print("hi there")
                





print(fun(1))

