for i in range(int(input())):
    a = input()
    if a.count('1') == 0:
        print('Beginner')
    elif a.count('1') == 1:
        print('Junior Developer')
    elif a.count('1') == 2:
        print('Middle Developer')
    elif a.count('1') == 3:
        print("Senior Developer")
    elif a.count('1') == 4:
        print("Hacker")
    elif a.count('1') == 5:
        print("Jeff Dean")
