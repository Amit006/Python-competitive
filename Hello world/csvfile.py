import csv

#open a file
with open("note.txt", 'r') as textfile:
    linelist = csv.reader(textfile)

    for line_num in linelist:
       print(','.join(line_num))
       print("hello hello")
