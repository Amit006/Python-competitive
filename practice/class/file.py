# with read and write files of the Containe
file_name = input("Enter the File Name:")

file_op = open(file_name,'a+')
file_data = file_op.readline()
print("******file data ***** \n",file_data)
# file_op = open(file_name,'a+')
input_file = input("enter someting on the File")
file_op.write(input_file)
# file_op = open(file_name,'r')
file_data = file_op.readline()
print("contain of the Files is:\n",file_data)


