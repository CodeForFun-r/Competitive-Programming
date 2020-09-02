for t in range(int(input())):
    n = int(input())
    c, i, t = 0, 1, n
    
    while t >= 1:
        t = n // pow(5, i)
        c = c + t
        i = i + 1
        
    print(c)
