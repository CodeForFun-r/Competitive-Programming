for t in range(int(input())):
    n = int(input())
    num = sorted([int(x) for x in input().split(' ')])
    l = []
    
    i = 0
    while i < (n - 1):
        l.append(abs(num[i] - num[i + 1]))
        i = i + 1
    
    print(min(l))
