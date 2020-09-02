for i in range(int(input())):
    d1, d2, d3, d4, d5 = 0, 0, 0, 0, 0
    n = int(input())
    f = lambda x, y: (int(x / y), (x - (int(x / y) * y)))
    if n >= 100:
        d1, n = f(n, 100)
    if n >= 50:
        d2, n = f(n, 50)
    if n >= 10:
        d3, n = f(n, 10)
    if n >= 5:
        d4, n = f(n, 5)
    if n >= 2:
        d5, n = f(n, 2)
    print(d1 + d2 + d3 + d4 + d5 + n)
