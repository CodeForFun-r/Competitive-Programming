for t in range(int(input())):
    n, q = map(int, input().split(' '))
    
    s, prev = 0, 0
    
    for i in range(q):
        o, d = map(int, input().split(' '))
        
        if prev == o:
            s = s + abs(d - o)
        else:
            s = s + abs(prev - o) + abs(d - o)
            
        prev = d
        
    print(s)
