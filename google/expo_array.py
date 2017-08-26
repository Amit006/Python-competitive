a=[1,2,3,9]
b=[1,2,3,4,4]
sum=8
first,second =0,0
Pairs_2_Arrays=[(x,y) for x in a for y in b if x!=y]
print("pairs os array", Pairs_2_Arrays)
print("len of the array:", len(Pairs_2_Arrays))

def disply_Pairs(Pairs_2_Arrays,sum):
    print("*****printing the pairs of array:*********")
    for i in range(0,len(Pairs_2_Arrays)-1):
        print("printing the value of 1st index:",i)
        for j in range(0,2):
            print("printing the values of j:",j)
            print("printing the  values of the array result[][]::",Pairs_2_Arrays[i][j])
            print("\n")
            if(j==0):
                fist=Pairs_2_Arrays[i][j]
                print("1st:",fist)
            else:
                second=Pairs_2_Arrays[i][j]
                print("2nd",second)

            def sum(x,y):
                return x+y
            pairs=sum(fist,second)
            if(pairs==sum):
                return True 
            else:
                return False





disply_Pairs(Pairs_2_Arrays,sum)
