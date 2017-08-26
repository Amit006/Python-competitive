def Lear_aearch(my_item,the_list):
    position = 0
    found = False
    while position < len(the_list)and not found:
        if the_list[position]==my_item:
            found = True
        position+=1
    return found

if __name__=="__main__":
    contain_list = ["banana","mango","Chocolate","pikels"]
    item=input("enter what to Find")
    msg=Lear_aearch(item,contain_list)
    if msg:
        print('conatin is found')
    else:
        print('conatn not found')
        
            
        
