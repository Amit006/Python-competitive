a=[66.6,333,333,1,1.2543]
print("Counting. the Spacific Variable:", a.count(66.6), a.count(333))

print("result insert:",a.insert(2,-1))
print("result append:",a.append(333))
print("result ",a)
print("result index",a.index(333))
print("result remove",a.remove(333))
print("a before reverse:a[]", a)
print(a.reverse())
print("after reverse a[]",a)
print(a.sort())
print("after sort: a[]", a)
print(a.pop())
print("after poping the firest element:a[]" ,a)

print("\n ****list using as stack*** \n")
stack =[3,4,5]
print("stack[]:",stack)
stack.append(6)
stack.append(7)
print("stack[]",stack)
print("stack.pop:",stack.pop())
print("stack.pop:",stack.pop())
print("stack[]:",stack)

#list as queue 
print("\n ****using list as queues***\n")
from collections import deque
queue=deque(["erick","jhon","mikel"])
print("total queue",queue)
queue.append("jason")
queue.append("frost")
print("poping from left of the queue:",queue.popleft())
print("poping from right of the queue:",queue.popleft())

#List Comprehensions
squares = []
for x in range(10):
     squares.append(x**2)

print("squares[]:",squares)
#calculating the same thing inline
squares = list(map(lambda x: x**2, range(10)))
print("list(map(lamda x: x**2(squares[]:",squares)
squares=[]
squares = [x**2 for x in range(10)]
print("x**2 with for squares[]:",squares)

squares1= [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print("squares1[]:",squares1)
#equivalent to 
combs=[]
for x in [1,2,3]:
     for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
            print(combs)
print("before flatten combs", combs)
combs=[num for element in combs for num in element]
print("after flatten combs:",combs)
#string using 
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
fruit=[weapon for weapon in freshfruit]
print("fruit array[]:",fruit)
# create a list of 2-tuples like (number, square)
tuples=[(x, x**2) for x in range(6)]
print("tupes[]:",tuples)

#matrix problem 
print("####--MATIX PROBLEB--####")
transposed_matrix=[]
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
print("transposed matrix[]:",transposed_matrix)
#outher way
transposed=[]
for i in range(4):
    transposed.append([row[i] for row in matrix])

print("transpose[]:",transposed)

print("using zip functions")
transposed=list(zip(*matrix))
print("zip transposed matrix:",transposed)



