from collections import deque

file = open("9-1.in", "r")

for line in file:
    tokens = line.strip().split()
    players = int(tokens[0])
    scores = [0 for x in range(players)]
    last = int(tokens[6]) * 100

circle = deque([0])
player = 0
for m in range(1, last):
    if m % 23 == 0:
        circle.rotate(7)
        scores[player] += m + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(m)

    player = ((player+1) % players)

print(max(scores))
