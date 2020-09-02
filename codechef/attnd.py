for t in range(int(input())):
    s1 = ''
    
    for n in range(int(input())):
        if n == 0:
            s1 = input()
        else:
            s1 = s1 + '  ' + input()
    
    for s in s1.split('  '):
        if s1.count(s.split(' ')[0]) > 1:
            print(s)
        else:
            print(s.split(' ')[0])
