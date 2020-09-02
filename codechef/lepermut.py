for t in range(int(input())):
    n = int(input())
    p = list(map(int, input().split(' ')))
    ci, cli = 0, 0
    
    for i in range(n):
        for j in range(i+1, n):
            if p[i] > p[j]:
                ci = ci + 1
                
    for i in range(n-1):
        if p[i] > p[i+1]:
            cli = cli + 1
            
    if ci == cli:
        print('YES')
    else:
        print('NO')
