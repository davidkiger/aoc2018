file = open("6-1.in", "r")


def find_closest(end_points, x, y):
    total_dist = 0
    for point in end_points:
        dist = abs(x - point[0]) + abs(y - point[1])
        total_dist += dist

    if total_dist < 10000:
        return True

    return False


grid = [['.' for i in range(360)] for j in range(360)]
end_points = []
markers = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
i = 0

for line in file:
    x, y = line.strip().split(', ')
    grid[int(x)][int(y)] = markers[i]
    end_points.append((int(x), int(y)))
    i += 1

group_size = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if find_closest(end_points, x, y):
            group_size += 1

print(group_size)
