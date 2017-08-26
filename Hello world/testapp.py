# x = 5
# y = x + 3
# y = int(str(y)+"2")
# print(y)
# List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# if int(List) % 2 == 0:
#     print(List[List[List[4]]])
# else:
#     x += 7
#     print(x)


# class Car(object):
#     print('on the class call')
#
#     def __init__(self, model):
#         self.model = model
#         print("model value would be:"+self.model)
#
# C1 = Car('bmw')
# C1.model

# addition with exception

# i = int(input("Enter your 1st number::"))
# j = int(input("Enter your 2nd number::"))


class ADD(object):
   try:
       def Display(self, i, k):
                self.i = i
                self.k = k
                c = i + k
                print("Result of your add number is::%d " % c)
   except TypeError:
           print("look carefully u r adding sting into the position of number")
   finally:
          print("u must enter two number beside integer")

a = ADD()
a.Display(4.6, "Amo")

