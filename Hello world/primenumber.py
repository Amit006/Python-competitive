n = 999999

prime = []
for i in range(2, n):
    print('Value of i is ::', i)
    for x in range(2, i):
        print('value of X is::', x)
        if i % x == 0:
            print(i, 'equals to', x, i // x)
        else:
            print(i, 'IS AN PRIME NUMBER', prime.append(i))

print(prime.sort(), prime)
