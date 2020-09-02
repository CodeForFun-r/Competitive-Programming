for t in range(int(input())):
    q, p = map(int, input().split(' '))
    amount = float(q * p)
    if q > 1000:
        amount = amount - (amount * 0.1)
        print(f'{amount:.6f}')
    else:
        print(f'{amount:.6f}')
