for x in range(1,11):
    
    print(repr(x).rjust(4),repr(x*x).rjust(0), end= ' ')
	# note use of 'end' on privious line
    print(repr(x*x*x).rjust(0))