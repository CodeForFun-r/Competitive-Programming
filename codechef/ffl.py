from collections import defaultdict

for t in range(int(input())):
    n, s = map(int, input().split(' '))
    p = list(map(int, input().split(' ')))
    b = input().split(' ')
    
    d = defaultdict(list)
    
    for i, j in zip(p, b):
        d[j].append(i)
 
    
    if (not d['0']) or (not d['1']) or (s + (min(d['0']) + min(d['1']))) > 100:
        print('no')
    else:
        print('yes')
