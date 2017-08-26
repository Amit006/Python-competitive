num = input("Enter the number:")
strlenth = len(num)
for i in range(strlenth):
    for j in range(strlenth - i):
        print(num[j], end="\t")
    print("end of 2nd loop:")