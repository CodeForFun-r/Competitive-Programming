for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(' ')))
    l.sort(reverse=True)
    
    s = 0
    
    for i, e in enumerate(l):
        if e - i > 0:
            s = (s + e - i) % (pow(10, 9) + 7)
    
    print(s)
