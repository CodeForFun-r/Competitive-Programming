player1, player2 = [], []
csum1, csum2 = 0, 0
maximum = 0
for i in range(int(input())):
    score1, score2  = map(int, input().split(' '))
    csum1 = csum1 + score1
    csum2 = csum2 + score2
    lead = abs(csum1 - csum2)
    if lead > maximum:
        winner = 1 if csum1 > csum2 else 2
        maximum = lead

print(winner, maximum)
