house = []
side1 = []
side2 = []

N = int(input())
m, c = map(int, input().split(' '))

for i in range(N):
    house.append([int(a) for a in input().split(' ')])

h1 = house[0]
side1.append(h1)

line = lambda x, y: (m * x) - y + c

j = 1
while j < N:
    h = house[j]
    res1 = line(h1[0], h1[1])
    res2 = line(h[0], h[1])
    sign = res1 / res2
    if sign > 0:
        side1.append(h)
    else:
        side2.append(h)
    j = j + 1

extract = lambda s: s[2]
    
print(max(sum(map(extract, side1)) , sum(map(extract, side2))))

