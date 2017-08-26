__author__ = 'FRODT'
print("**************PYTHON EXPERIMENT***************")
x = 5
index = 0
element = 0
my_string = "HELLO"
if x < 5:
    print("Hello world")
elif 5 == x:
    print("HI i am groot")
else:
    print("hI THERE")
vendor = ["Cisco", "Sumit", "Amit", "sellesman"]
for each_vendor in vendor:
    print('the vendor are::', each_vendor)
    print(vendor)
for latter in my_string:
    print(latter)
    print(latter * 2)
    print(latter * 10)
for index, element in enumerate(vendor):

    print("index is %d" % index)
    print("Element is %s" % element)

