name = input(str("enter some string"))
unique =[]
for i in name:
    if i not in unique:
        unique.append(i)
if unique == name:
    print("Strin  Has double charator ")
else:
    print("string has some double charator")