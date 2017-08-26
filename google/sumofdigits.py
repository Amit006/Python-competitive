

a=[1,2,3,9]
b=[1,2,4,4]
sum= 8;
def sumofpairs(a,sum):
        for i in range(0,len(a)):
                # print("1st Contain of a[i]",a[i])
                for j in range(len(a)-1,-1,-1):
                        # print("2nd contend of a[i]:",a[i])
                        # print("2end Contains of a[j]",a[j])
                        if(a[i]+a[j]==8):
                                # print(" a[] is true")
                                flag=1
                                break
                        else:
                                # print("b[] is false")
                                flag=0
                # print("1st Contains of a[j]",a[j])
        if(flag==0):
                print("false")
        else:
                print("true")


sumofpairs(a,sum)
sumofpairs(b,sum)    