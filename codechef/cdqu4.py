for t in range(int(input())):
    string = input()
    substring = input()
    newstring = string.replace(substring, '')
    print(newstring) if len(newstring) > 0 else print('0')
