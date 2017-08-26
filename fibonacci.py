# fc = int(input('enter the number boundary::'))
# i =1
# c=0
# first,second=1,1
# print(first,second)
# for i in range(1,fc):
#     
#     c= first + second 
#     first = second
#     second= first + i
#     print(c)
# print ("hi the6re") 
from symbol import argument
i=int(input("Enter your 1st number::"))
j=int(input("Enter your 2nd number::"))
class ADD(object):
    try:
        def Display(self):
            c =i + j 
            print ("Result of your add number is::",c)     
    except ValueError , argument:
        print("look carefully", argument) 
    


a = ADD
a.Display()

