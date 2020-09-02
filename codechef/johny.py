for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split(' ')))
    k = int(input()) - 1
    print((sorted(a).index(a[k])) + 1)
