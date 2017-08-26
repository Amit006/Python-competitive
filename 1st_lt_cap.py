string=input('Enter a sentence/sentences please:')
sentence=string.split('.')
for i in sentence:
    print i.strip().capitalize()+". ",end = ''
