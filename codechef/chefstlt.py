for i in range(int(input())):
    s1 = input()
    s2 = input()
    e1 = 0
    e2 = 0
    for i, j in zip(s1, s2):
        if i != '?' and i == j:
            e1 = e1 + 1
        if i == '?' or j == '?':
            e2 = e2 + 1
    print(len(s1) - e2 - e1, len(s1) - e1)
