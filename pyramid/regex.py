import re
regex = re.compile(r'(\d+)|([\+-]?\d+)')
s = "1 2 3 4 5 6 +1 +2 +3 -1 -2 -3+654 -789 321"
for r in regex.findall(s):
    if r[0]:
        # whole (unsigned)
        print('whole', r[0])
    elif r[1]:
        # signed (integer)
        print('signed', r[1])



