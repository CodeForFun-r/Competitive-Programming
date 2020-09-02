for t in range(int(input())):
    s = input()
    n = len(s)
    c, i = 0, 0

    while i < n:
        try:
            if (s[i] == 'x' and s[i+1] == 'y') or (s[i] == 'y' and s[i+1] == 'x'):
                c = c + 1
                i = i + 2
            else:
                i = i + 1
        except:
            break
    print(c)
