x = int(raw_input('enter the number'))
ans = 0
while ans**3 < abs(x):
        ans = ans +1
        print ans
if ans**3 != abs(x):
        print x, 'is not a perfect cube'
else:
        if x < 0:
            ans =-ans
            print 'cube root of ' + str(x) + 'is' + str(ans)
        
