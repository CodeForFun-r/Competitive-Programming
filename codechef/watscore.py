from collections import defaultdict
for i in range(int(input())):
    score = defaultdict(list)    
    for j in range(int(input())):
        a, b = map(int, input().split(' '))
        if a <= 8:
            score[a].append(b)
    score = dict(score)
    keys = list(score)
    max_score = [max(score[key]) for key in keys ]
    print(sum(max_score))
