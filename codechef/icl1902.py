from math import sqrt
for i in range(int(input().strip())):
    n = int(input().strip())
    s = 0
    while n != 0:
        s = s + 1
        n = n - (int(sqrt(n)) ** 2)
    print(s)
