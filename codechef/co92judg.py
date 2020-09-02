for t in range(int(input())):
    n = int(input())    
    
    a = [int(x) for x in input().split(' ')]
    b = [int(x) for x in input().split(' ')]
    
    a_max, b_max = max(a), max(b)
    a_sum, b_sum = sum(a), sum(b)
    
    if (a_sum - a_max) < (b_sum - b_max):
        print('Alice')
    elif (a_sum - a_max) > (b_sum - b_max):
        print('Bob')
    else:
        print('Draw')
