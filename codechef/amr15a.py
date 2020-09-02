n = int(input())
a = map(int, input().split(' '))
even, odd = 0, 0

for i in a:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
        
print('READY FOR BATTLE') if even > odd else print("NOT READY")
