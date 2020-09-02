for t in range(int(input())):
    l, r = map(int, input().split(' '))
    c = 0
    d = {'2':True, '3':True, '9':True}
    for i in range(l, r+1):
        if (d.get(str(i)[-1], False)):
            c = c + 1
    print(c)
