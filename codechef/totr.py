n, m = input().split(' ')
l1 = list(m)
l2 = list(m.swapcase())
d = {}

for i, j in zip("abcdefghijklmnopqrstuvwxyz", l1):
    d[i] = j

for i, j in zip("abcdefghijklmnopqrstuvwxyz".swapcase(), l2):
    d[i] = j
    
d['_'] = ' '
d['.'] = '.'
d[','] = ','
d['!'] = '!'
d['?'] = '?'

l3 = [input() for i in range(int(n))]

for i in l3:
    s = ''
    for j in i:
        s = s + d[j]
    print(s)
