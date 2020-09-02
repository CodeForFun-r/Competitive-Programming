n = int(input())

while(n>0):
    num_string = str(input())
    l = []
    my_string = ""
    for sp in num_string:
        if sp == ' ':
            l.append(my_string)
            my_string = ""
        else:
            my_string = my_string + sp
    l.append(my_string)
    i = int(l[0])
    j = int(l[1])
    k = int(l[2])
    
    if (i>j) and (i>k) :
        if (j>k):
            print(j)
        else:
            print(k)
    elif j>k:
        if (i>k):
            print(i)
        else:
            print(k)
    else:
        if (i>j):
            print(i)
        else:
            print(j)
    n = n-1
