import operator 
a=input("Enter the String:")
count=0
for i in range(0,len(a)):
    if (a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u"):
                print("vowel in ur string:", a[i])
                count+=1


print("vowel ocuare in the programme {}:",count)

# Program to count the number of each vowel in a string

# # string of vowels
# vowels = 'aeiou'

# # change this value for a different result
# ip_str = 'Hello, have you tried our turorial section yet?'

# # uncomment to take input from the user
# #ip_str = input("Enter a string: ")

# # make it suitable for caseless comparisions
# ip_str = ip_str.casefold()
# print("string assertation by casefold:",ip_str)

# # make a dictionary with each vowel a key or value 0
# count = {}.fromkeys(vowels,0)
# print("assign the keys of dictionary:",count)
# # count the vowels
# for char in ip_str:
#    if char in count:
#        count[char] += 1
 
# print(count)