for t in range(int(input())):
    n = int(input())
    g = input()
    
    if (g.count('N') == n) or (g.count('Y') and g.count('I')):
        print('NOT SURE')
        
    if (g.count('I')):
        print('INDIAN')
        
    if (g.count('Y')):
        print('NOT INDIAN')
