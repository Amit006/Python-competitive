# coding=utf-8
num=int(input("enter the number:"))

if (num > 0):
    print("printing num > o:")
    for i in range(num):
        for j in range(num - i):
            print(j, end='\t')
    print('', end ='\n ')




if (num < 0):
    print("printing num < 0 ")
    for i in range(num):
        for j in range(num + i):
            print(j, end='\t')