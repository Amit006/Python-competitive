

def ROOT_mul():
    a = int(input("1st num:"))
    b = int(input("2nd num :"))
    p1= int(input("1st num power:"))
    p2 = int(input("2nd num power:"))
    fast = a**p1
    second = b ** p2
    result = int(fast * second);
    print("result: {}".format(result)) 


ROOT_mul()