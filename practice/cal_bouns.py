# def calculate_bouns(amt, rate=3.4, term=1):
#     	total=amt+(amt*rate*term)
# 		return total


def calculate_bouns(amt, rate=3.4, term=1):
	total=amt + (amt * rate * term )
	return total

print(calculate_bouns(1000))
print(calculate_bouns(1000, 4))
print(calculate_bouns(1000, 4, 2))
print(calculate_bouns(rate=13, amt=3000, term=6))

