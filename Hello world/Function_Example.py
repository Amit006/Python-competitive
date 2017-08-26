# def getMassage(name):
#    message = 'hello , ' + name
#    return message
#
# def printMessage(message):
#       print(message)
#       return
#
# output = getMassage('Amit Nayek')
# printMessage(output)

def main():
   print("main")
   name = Getnames()
   printName(name)
   return

print("hello world")


def Getnames():
     print("getnames")
     names = ['Amit', 'Rahul', 'Sumit', 'joyfull']
     newName = input("Enter the new name::")
     names.append(newName)
     return names


def printName(names):
  print(names)
  for name in range(5):
    Name_char = names.index(name)
    print(Name_char)
    return


main()
