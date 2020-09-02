from collections import Counter

for t in range(int(input())):
    n, q = map(int, input().split(' '))
    s = input()
    d = Counter(s)
    val = list(d.values())
        
    for i in range(q):
        c = int(input())
        print(sum(j - c for j in val if j - c > 0))
