class b(Exception):
    pass

class c(b):
    pass

class d(c):
    pass

for cls in [d,c,b]:
    try:
    	raise cls
	#raise cls()
    except d:
       print("d class")
       print("from except d")
    except c:
       print("c class")
       print("from except c")
    except b:
       print("b class")
       print("from except b")

