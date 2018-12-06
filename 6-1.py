file = open("6-1.in", "r")


def find_closest(end_points, x, y):
    min_dist = 1000000
    i = 0
    key = 0
    count = 0
    for point in end_points:
        dist = abs(x - point[0]) + abs(y - point[1])
        if dist < min_dist:
            min_dist = dist
            count = 1
            key = i
        elif dist == min_dist:
            count += 1
        i += 1

    if count == 1:
        return key
    else:
        return -1


grid = [['.' for i in range(360)] for j in range(360)]
end_points = []
markers = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
i = 0

for line in file:
    x, y = line.strip().split(', ')
    grid[int(x)][int(y)] = markers[i]
    end_points.append((int(x), int(y)))
    i += 1

for x in range(len(grid)):
    for y in range(len(grid[x])):
        c = find_closest(end_points, x, y)
        if c != -1:
            grid[x][y] = markers[c]

sums = []
for i in range(len(markers)):
    total = sum(x.count(markers[i]) for x in grid)
    for k in range(len(grid)):
        if grid[k][0] == markers[i]:
            total = 0
        if grid[k][len(grid)-1] == markers[i]:
            total = 0
        if grid[len(grid)-1][k] == markers[i]:
            total = 0
        if grid[0][k] == markers[i]:
            total = 0
    sums.append(total)

print(max(sums))
