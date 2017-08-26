import string

def isPanagram(str1,alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    print(alphaset)
    str1_lower=set(str1.lower())
    if(alphaset <= str1_lower):
       print("compared match %s" %alphaset)
       print("compared match %s" %str1_lower)
    else:
       printf("string is not match")

       
isPanagram("hi there its coold")
isPanagram("the quick brown  fox jumps over the lazy dog")
