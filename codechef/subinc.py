for t in range(int(input())):
    n = int(input())
    array = list(map(int, input().split(' ')))
    d = {0:1}
    
    for i in range(1, n):
        if array[i] >= array[i-1]:
            d[i] = d[i-1] + 1
        else:
            d[i] = 1
            
    print(sum(d.values()))
