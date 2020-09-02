for i in range(int(input())):
    a, b = map(int, input().split(' '))
    s = a + b
    s = list(str(s))
    n = 0
    for i in s:
        if i == '0':
            n = n + 6
        if i == '1':
            n = n + 2
        if i == '2':
            n = n + 5
        if i == '3':
            n = n + 5
        if i == '4':
            n = n + 4
        if i == '5':
            n = n + 5
        if i == '6':
            n = n + 6
        if i == '7':
            n = n + 3
        if i == '8':
            n = n + 7
        if i == '9':
            n = n + 6
    print(n)
