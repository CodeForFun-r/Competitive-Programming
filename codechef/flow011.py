for t in range(int(input())):
    n = int(input())
    hra, da = 0, 0
    if n < 1500:
        hra = 0.1 * n
        da = 0.9 * n
    else:
        hra = 500
        da = 0.98 * n
        
    print(n + hra + da)
