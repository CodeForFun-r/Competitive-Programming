import re

p = re.compile('1 (0 ){0,4}1')

for t in range(int(input())):
    n = int(input())
    if not p.search(input()):
        print('YES')
    else:
        print('NO')
