for i in range(int(input())):
    swap = 0
    n = int(input())
    a = input()
    b = a.split(' ')
    max_count = max(b, key = lambda x: b.count(x))
    for i in b:
        if i != max_count:
            swap = swap + 1
    print(swap)
