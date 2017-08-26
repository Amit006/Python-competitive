count={"upper":0,"lower": 0}
def Cap_Small_Check(str1):
    
    for i in str1:
        if(i.isupper()):
            count["upper"]+=1
        else:
            count["lower"]+=1


text=open("sample.txt")
msg=text.readline()
print(msg);
Cap_Small_Check(msg)
print("the number of upper Charatrs:{} or lower characters:{}".format(count["upper"],count["lower"]))    

