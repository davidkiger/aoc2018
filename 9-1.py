file = open("9-1.in", "r")

for line in file:
    tokens = line.strip().split()
    players = int(tokens[0])
    scores = [0 for x in range(players)]
    last = int(tokens[6])

circle = [0]
idx = 0
player = 0
for m in range(1, last):
    if m % 23 == 0:
        to_remove = (idx - 7) % len(circle)
        scores[player] += m + circle[to_remove]
        circle.pop(to_remove)
        idx = to_remove
    else:
        circle.insert((idx+2) % len(circle), m)
        idx = circle.index(m)

    player = ((player+1) % players)

print(max(scores))
