def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
    
for i in range(int(input())):
    a, b = map(int, input().split(' '))
    j = 1
    while(not prime(a+b+j)):
        j = j + 1
    print(j)
