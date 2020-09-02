for t in range(int(input())):
    n, k = map(int, input().split(' '))
    l = list(range(1, n + 1))
    
    if k < n - 1:
        for i in range(k + 1):
            l[0], l[n - i - 1] = l[n - i - 1], l[0]
        
    print(' '.join(map(str, l)))
