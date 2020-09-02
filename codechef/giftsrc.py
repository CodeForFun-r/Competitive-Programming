d = { 'L': (-1, 0),
      'R': (1, 0),
      'U': (0, 1),
      'D': (0, -1)
     }

for t in range(int(input().strip())):
    n = int(input().strip())
    s = input()
    i = 0
    c = (0, 0)
    while i < n:
        if (d[s[i]][0] == d[s[i-1]][0] or d[s[i]][1] == d[s[i-1]][1]) and i != 0:
            i = i + 1
            continue
        else:
            c = c[0] + d[s[i]][0], c[1] + d[s[i]][1]
            i = i + 1
    print(c[0], c[1])
