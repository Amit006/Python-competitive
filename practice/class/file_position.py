#!/usr/bin/python

# Open a file
fo = open("sample.txt", "r+")
str = fo.read(10);
print ("Read String is : ", str)

# Check current position
position = fo.tell();
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
print(position)
str = fo.read(10);
print ("Again read String is : ", str)
# Close opend file
fo.close()
