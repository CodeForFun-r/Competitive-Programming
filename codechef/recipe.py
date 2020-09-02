from functools import reduce
from math import gcd

for t in range(int(input())):
    a = list(map(int, input().split(' ')))
    r = reduce(gcd, a[1:])
    print(*[ i // r for i in a[1:] ])
