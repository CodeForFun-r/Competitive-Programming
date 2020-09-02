for i in range(int(input())):
    n = int(input())
    if n % 10 == 0:
        print(0)
    elif n % 5 == 0:
        count = 0
        while not (n % 10 == 0):
            count = count + 1
            n = n * 2
        print(count)
    else:
        print(-1)
