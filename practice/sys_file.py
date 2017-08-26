import sys

try:
    f = open('sample.txt')
    s = f.readline()
    #i = str(s.strip())
    i= int(s.strip())
    print("contain of the variable:",i)
except OSError as err:
    print("os error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected erro;".sys.exc_info()[0])
    raise
