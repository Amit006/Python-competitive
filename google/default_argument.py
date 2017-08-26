def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        msg = prompt
        if msg in ('y', 'ye', 'yes'):
            return True
        if msg in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if(retries < 0):
            raise IOError('refusenik user')
        print(complaint)

ask_ok('y')
ask_ok('yes')
ask_ok('ye')
if __name__ == '__main__':
    ask_ok('y')

#how to call this function 

