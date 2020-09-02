n, q = map(int, input().strip(' ').split(' '))
d = sorted(list(map(int, input().strip(' ').split(' '))))

def search(e, a, length):
    start = 0
    end = length - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == e:
            return e
        elif e > a[mid]:
            start = mid + 1
        elif e < a[mid]:
            end = mid - 1
    if e < a[end]:
        return a[start]
    else:
        return a[end]

for _ in range(q):
    s = int(input().strip(' '))
    if s < d[0]:
        print(-1)
    else:
        print(search(s, d, n))
