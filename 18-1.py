from copy import deepcopy

file = open("18-1.in", "r")

acre = []
for line in file:
    acre.append(list(line.strip()))

for minute in range(10):
    new_acre = deepcopy(acre)

    for y, row in enumerate(acre):
        for x, spot in enumerate(row):
            neighbors = []
            if y > 0 and x > 0: neighbors.append(acre[y-1][x-1])
            if y > 0: neighbors.append(acre[y-1][x])
            if y > 0 and x < len(row)-1: neighbors.append(acre[y-1][x+1])
            if x > 0: neighbors.append(acre[y][x-1])
            if x < len(row)-1: neighbors.append(acre[y][x+1])
            if y < len(row)-1 and x > 0: neighbors.append(acre[y+1][x-1])
            if y < len(row)-1: neighbors.append(acre[y+1][x])
            if y < len(row)-1 and x < len(row)-1: neighbors.append(acre[y+1][x+1])

            if spot == '.' and neighbors.count('|') >= 3:
                new_acre[y][x] = '|'
            elif spot == '|' and neighbors.count('#') >= 3:
                new_acre[y][x] = '#'
            elif spot == '#' and not (neighbors.count('#') >= 1 and neighbors.count('|') >= 1):
                new_acre[y][x] = '.'

    acre = new_acre

print(sum(x.count('#') for x in acre) * sum(x.count('|') for x in acre))
