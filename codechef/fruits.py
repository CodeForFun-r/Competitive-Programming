for t in range(int(input())):
    n, m, k = map(int, input().split(' '))
    small = min(n, m)
    diff = abs(n - m)
    
    if diff <= k:
        print(0)
    else:
        print(diff - k)
