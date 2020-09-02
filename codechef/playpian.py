for i in range(int(input())):
    n = 0
    prev = ''
    
    for s in input():
        if n == 0:
            prev = s
            n = n + 1
            continue
            
            
        if n == 1:
            if prev == s:
                print('no')
                break
                
            n = n + 1
        
        if n > 1:
            n = 0
    else:
        print('yes')
        
