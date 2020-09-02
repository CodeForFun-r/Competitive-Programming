for t in range(int(input())):
    n, k = map(int, input().split(' '))
    p = map(int, input().split(' '))
    print(sum(i-k for i in p if i > k))
