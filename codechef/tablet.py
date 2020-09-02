for i in range(int(input())):    
    n, b = map(int, input().split(' '))
    a = 0

    for j in range(n):
        w, h, p = map(int, input().split(' '))
        if b >= p:
            if (w * h) > a:
                a = w * h
    
    print(a) if a > 0 else print('no tablet')
