from math import gcd

for t in range(int(input())):
    a, b = map(int, input().split(' '))
    
    g = gcd(a, b)
    
    if g == 1:
        l = a * b
    else:
        x, y = a // g, b // g
        l = x * y * g
        
    print(g, l)

