for i in range(int(input())):
    a, b = map(int, input().split(' '))
    for i in range(a):
        b = sum(range(b + 1))
    print(b)
