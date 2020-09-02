import math
for i in range(int(input())):
    try:
         number = int(input())
    except EOFError:
         number = 0
    if number:
         print(int(math.sqrt(number)))

