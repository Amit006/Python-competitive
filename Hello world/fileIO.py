file_name = "note.txt"
write = 'w'
append = 'a'

data = input("enter some data into file::::")

file = open (file_name, mode=write)
file.write("this is first line \n")
file.write("this is a Second  line \n")
file.write(data)
file.close()

print("file is being successfully written ")

# read all file content

onefile = open ("note.txt", "r")
allFileContent = onefile.read()
print(allFileContent)
# reading one lines of the files
firstline = onefile.readline()
print(firstline)
secondline = onefile.readline()
print(secondline)
boolean_readable = onefile.readable()
print("alllines :\n ",boolean_readable)
