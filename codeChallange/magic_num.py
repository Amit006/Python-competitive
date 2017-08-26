PList=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
   
def countFunction(N,L,R):
    CountList=[]
    PmiList=[]
    for p in range(2,N+1):
        if(p in PList):
            PmiList.append(p)

    k=0
    while k < len(PmiList):
        for i in range(L,R+1):   #CountList = [i for i in range(l,R+1) if i % PmiList[k] == 0 && i not in CountList]
            if(i % PmiList[k] == 0) and i not in CountList:
                CountList.append(i)
        k=k+1
    return len(CountList)

T=int(input())
i=0
while i<T:
    N,L,R=map(int,(input()).strip().split())
    print (countFunction(N,L,R))
    i=i+1