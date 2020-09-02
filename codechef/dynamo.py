for t in range(int(input())):
    N = int(input())
    a = int(input())
    s = pow(10, N) + pow(10, N) + a
    print(s, flush=True)
    b = int(input())
    c = pow(10, N) - b
    print(c, flush=True)
    d = int(input())
    e = s - (a + b + c + d)
    print(e, flush=True)
    o = int(input())
