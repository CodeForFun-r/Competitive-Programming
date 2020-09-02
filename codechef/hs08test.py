def parts(name):
    l=[]
    string = ''
    for n in name:
        if n == ' ':
            l.append(string)
            string = ''
        else:
            string = string + n
    l.append(string)
    return l
    
def trans(my_list):
    i = float(my_list[0])
    j = float(my_list[1])
    if j>=i+0.50 and ((i%5) == 0):
        temp = j-i-0.50
        print("%.2f" %temp)
    else:
        print("%.2f" %j)
        
x = str(input())
l1 = parts(x)
trans(l1)
