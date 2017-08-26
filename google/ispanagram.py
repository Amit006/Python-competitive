import string

def isPanagram(str1,alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    print(alphaset)
    str1_lower=set(str1.lower())
    if(alphaset <= str1_lower):
       print("string is match")
       print("1st string  {}".format(alphaset))
       print("2nd string  {}" .format(str1_lower))
    else:
       print("string is not match")

       
isPanagram("hi there its coold")
isPanagram("the quick brown  fox jumps over the lazy dog")
