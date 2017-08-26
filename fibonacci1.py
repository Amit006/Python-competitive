# fibonacci
fc = int(input('enter the number boundary::'))
i =0
j =1
for i in range(0,fc+1):
	if(i>fc):
	  j=j+i
	  j,i = i,j
	  print(+j)