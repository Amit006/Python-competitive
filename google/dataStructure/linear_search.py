data_list = [1,2,3,5,9,7,8,9,7,5,6,4,2,6]
print("****___linear search__****")
chose = "ser"
def delete_item():
    position = 0
    try:
        item = int(input("enter the item:"))
    except:
        print("=-----\tEnter a valid integer sir\t-----")
        item = int(input("Enter the valid number:"))
    finally:
        while(position < len(data_list)):
            if (data_list[position]==item):
                print("The Element is going to be deleted: ",data_list[position])
                permition = str(input("Are You Sure y/n:"))
                if(permition.startswith("y")):
                    delete_item=data_list[position]
                    del data_list[position]
                    print("deleted item in list[{}]={}".format(position,delete_item))
                    break
            else:
                position+=1
        print("The Item lsit[{}]={} none".format(position,data_list[position]))        


def Search(item):
    position = 0
    flag = True
    while(position<len(data_list)):
        if(data_list[position]==item):
            flag = True
        else:
            flag = False
        position =position + 1
    if (flag==True):
        print("Item is found :",data_list[position])
    else:
        print("Item is not found:",data_list[position]) 
        

def insert_item():
    size = int(input("\t **how many times you like to Enter:"))
    for i in range(0,size):
        data = int(input("enter a data into list:"))
        data_list.append(data)

def Disply():
    for i in data_list:
        print("\t [{}]".format(i))

def Select_choice():
    how_many = int(input("Enter how many times you want to operation:"))
    for i in range(1,how_many+1):
        
        print("**Enter --1(one)-- for insert:**")
        print("**Enter --two-- for Delete:**")
        print("**enter --three-- for Display:**")
    

if __name__=="__main__":
        Select_choice()
        chose = str(input("Enter your choice in string:"))
        if(chose.startswith("one")):
            insert_item()
        if(chose.startswith("two")):
            delete_item()
        if(chose.startswith("three")):
            Disply()
            
