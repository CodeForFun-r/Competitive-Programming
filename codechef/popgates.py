for t in range(int(input())):
    n, k = map(int, input().split(' '))
    s = input().split(' ')
    t2 = []
    t1 = s[:]
    
    for i in range(n):
        if s[i] == 'H':
            t2.append('T')
        else:
            t2.append('H')
    
    for i in range(n-1, n-k-1, -1):
        if s[i] == 'H':
            if s == t1:
                s = t2[:]
            else:
                s = t1[:]
    
    print((''.join(s)).count('H', 0, n-k))
