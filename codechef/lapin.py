for t in range(int(input())):
    s = input()
    n = len(s)
    
    if n % 2:
        l1, l2 = s[:n//2], s[(n//2) + 1:]        
        if sorted(l1) == sorted(l2):
            print('YES')
        else:
            print('NO')
            
    if not (n % 2):
        l1, l2 = s[:n//2], s[n//2:]
        if sorted(l1) == sorted(l2):
            print('YES')
        else:
            print('NO')
