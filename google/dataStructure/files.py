file_data=open("sample.txt")
data=file_data.readline()
print("printing files data::\n",data)
#printing the contains
msg=[]
for i in data:
	i+=i
	print("value of i ",i)
	print(i,end="")
	space=" "
	if(i==space):
	    print("your msg[] is:", msg.append(i))
	    print("printing the entire msg:",msg)
	else:
	   print("array msg[]:",msg)
	   print("msg[]  index is:",msg.index(i));

