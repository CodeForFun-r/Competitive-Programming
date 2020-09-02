from itertools import accumulate
from operator import mul
for i in range(int(input())):
    s = 0
    p = 1
    g = 0
    n = int(input())
    a = list(map(int, input().split(' ')))
    for i in range(n):
        s = accumulate(a[i:])
        p = accumulate(a[i:], mul)
        g =  g + [1 for j, k in zip(s, p) if j == k ].count(1)
    print(g)
