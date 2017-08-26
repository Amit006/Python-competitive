try:
	i=int(input("Enter your 1st number::"))
	j=int(input("Enter your 2nd numenr::"))
	class ADD(object):
		def display():
			c =i + j 
			print ("Result of your add number is::",c) 
	a = ADD
	a.display()
except IOError:
	print("look carefully you probubly miss 1 value in input")
else:
	print("its run sucessfully")



# diffrent type

i=int(input("Enter your 1st number::"))
j=int(input("Enter your 2nd numenr::"))
class ADD(object):
	try:
		def display():
			c =i + j 
			print ("Result of your add number is::",c)
	except IOError, ValueError, Argument:
		print("look carefully", Argument) 
	


a = ADD
a.display()

num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))