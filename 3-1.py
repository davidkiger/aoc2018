import re
file = open("3-1.in", "r")

grid = [[0 for i in range(1000)] for j in range(1000)]

for line in file:
    (num, _, l_offset, t_offset, w, h) = re.split(',| |x', line.strip().replace(':', '').replace('#', ''))

    l_offset = int(l_offset)
    t_offset = int(t_offset)
    w = int(w)
    h = int(h)
    for i in range(l_offset, l_offset+w):
        for j in range(t_offset, t_offset+h):
            grid[i][j] += 1

count = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1:
            count += 1

print(count)
