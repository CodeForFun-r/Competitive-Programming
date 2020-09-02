for t in range(int(input())):
    n, m = map(int, input().split(' '))
    s = -1
    
    for i in range(n):
        for j in range(m):
            if i == 0:
                s = s + 1
            else:
                s = s + 2
        s = s - 1
    
    print(s + 1)
