import fibo
fibo.fib(30)
fibo.fib2(60)
from fibo import fib,fib2

array=[]
a=fib(100)
b=fib2(200)
print("array append list:",array.append(a))
import sys
import builtins
fibo_function=[]
fibo_function.append(dir(builtins))
def Display_Array(Array_var):
    for i in Array_var:
        print("array[]:",i)

Display_Array(fibo_function)
print("dir functions:\n",fibo_function, end=" ")
print("\nfunctions of sys:\n",dir(sys) , end=" ")
print("\nfunctions of builtins:\n",dir(builtins) , end=" ")

