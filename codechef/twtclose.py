n, k = map(int, input().split(' '))

d = {}
c = 0

for i in range(k):
    s = input().split(' ')
    if s[0] == 'CLICK':
        if s[1] in d:
            c = c - 1
            del d[s[1]]
        else:
            d[s[1]] = 0
            c = c + 1
    elif s[0] == 'CLOSEALL':
        c = 0
        d = {}
    print(c)
