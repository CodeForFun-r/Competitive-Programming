for i in range(int(input())):
    num = input()
    if num == num[::-1]:
        print('wins')
    else:
        print('losses')
