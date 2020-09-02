for t in range(int(input())):
    l = []
    for i in range(int(input())):
        n = int(input())
        if n in l:
            l.remove(n)
        else:
            l.append(n)
    else:
        print(*l)
