for t in range(int(input())):
    n, k = map(int, input().split(' '))
    forget = input().split(' ')
    l = []
    
    for i in range(k):
        l.extend(input().split(' '))
        
    for w in forget:
        if w in l:
            print("YES", end = ' ')
        else:
            print('NO', end = ' ')
    
    print()
