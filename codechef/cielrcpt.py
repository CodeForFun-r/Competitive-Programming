for i in range(int(input())):
    p = int(input())
    s = 0
    n = 0
    
    while s < p:
        s = s + 2048
        n = n + 1
    
    if s == p:
        print(n)
        continue
    
    s = s - 2048
    n = n - 1
    
    while s < p:
        s = s + 1024
        n = n + 1

    if s == p:
        print(n)
        continue
        
    s = s - 1024
    n = n - 1
    
    while s < p:
        s = s + 512
        n = n + 1
    
    if s == p:
        print(n)
        continue
        
    s = s - 512
    n = n - 1
    
    while s < p:
        s = s + 256
        n = n + 1
 
    if s == p:
        print(n)
        continue
        
    s = s - 256
    n = n - 1
    
    while s < p:
        s = s + 128
        n = n + 1

    if s == p:
        print(n)
        continue
        
    s = s - 128
    n = n - 1
    
    while s < p:
        s = s + 64
        n = n + 1
    
    if s == p:
        print(n)
        continue
        
    s = s - 64
    n = n - 1
    
    while s < p:
        s = s + 32
        n = n + 1

    if s == p:
        print(n)
        continue
        
    s = s - 32
    n = n - 1
    
    while s < p:
        s = s + 16
        n = n + 1
    
    if s == p:
        print(n)
        continue
    
    s = s - 16
    n = n - 1
    
    while s < p:
        s = s + 8
        n = n + 1
        
    if s == p:
        print(n)
        continue
        
    s = s - 8
    n = n - 1
    
    while s < p:
        s = s + 4
        n = n + 1
        
    if s == p:
        print(n)
        continue
        
    s = s - 4
    n = n - 1
    
    while s < p:
        s = s + 2
        n = n + 1

    if s == p:
        print(n)
        continue
        
    s = s - 2
    n = n - 1
    
    while s < p:
        s = s + 1
        n = n + 1
        
    if s == p:
        print(n)
        continue
        
    n = n - 1
    
    print(n)
    
