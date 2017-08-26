a=[]
unique=[]

def takeing_input():
    for i in range(0,10):
        data=int (input("enter a number :"))
        a.append(data)
        print(data)



def algo_Unique(a,unique):
    for i in a:
        print("in for algo value of i",i)
        if(i not in unique):
             unique.append(i)


def display():
    for i in range(0,len(unique)):
        print("the unique list variable:{}",format(unique[i]))


takeing_input()
algo_Unique(a,unique)
display()
