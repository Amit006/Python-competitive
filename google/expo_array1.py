a=[1,2,3,9]
b=[1,2,3,4,4]
sum=8
first,second =0,0
Pairs_2_Arrays=[(x,y) for x in a for y in b if x!=y]

def SumofPairs(Pairs_2_Arrays,sum):
    for (x,y) in Pairs_2_Arrays:
        print("1st num:x",x)
        print("2nd number:y",y)
        print("\n")
        add=x+y
        if (sum==add):
            flag=1
        else:
            flag=0
    
    if(flag==0):
        print("false")
    else:
        print("True")

        

SumofPairs(Pairs_2_Arrays,sum)

