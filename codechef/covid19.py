for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))
    s = '1'
    
    i = 0
    while i < n-1:
        if a[i+1] - a[i] <= 2:
            s = s + '1'
        else:
            s = s + '01'
        
        i = i + 1
    
    l = s.split('0')
    q = []
    
    for i in l:
        q.append(len(i))
        
    print(min(q), max(q))
