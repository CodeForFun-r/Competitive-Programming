for t in range(int(input())):
    a, b, c = map(int, input().split(' '))
    print('YES') if a + b + c == 180 else print('NO')
