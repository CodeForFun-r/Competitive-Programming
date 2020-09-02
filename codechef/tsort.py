i = int(input())
my_list = []

while(i>0):
    num = int(input())
    my_list.append(num)
    i = i - 1

my_list.sort()

for j in my_list:
    print(j)
