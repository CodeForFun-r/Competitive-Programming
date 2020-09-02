for t in range(int(input())):
    n, k = map(int, input().split(' '))
    
    def f(x):
        global k
        if k >= x:
            k = k - x
            return 1
        return 0
    
    print(''.join(map(str,(map(f, map(int, input().split(' ')))))))
