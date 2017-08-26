def capitalize(string):
    return string.strip().title()

if __name__ == '__main__':
    string1 = str(input())
    capitalized_string = capitalize(string1)
    print(capitalized_string)
