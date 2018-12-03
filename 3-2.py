import re
file = open("3-1.in", "r")

grid = [[[] for i in range(1000)] for j in range(1000)]
no_overlaps = {}

for line in file:
    (num, _, l_offset, t_offset, w, h) = re.split(',| |x', line.strip().replace(':', '').replace('#', ''))

    l_offset = int(l_offset)
    t_offset = int(t_offset)
    w = int(w)
    h = int(h)
    no_overlaps[num] = True
    for i in range(l_offset, l_offset+w):
        for j in range(t_offset, t_offset+h):
            grid[i][j].append(num)

count = 0
for i in range(1000):
    for j in range(1000):
        if len(grid[i][j]) > 1:
            count += 1
            for x in grid[i][j]:
                no_overlaps[x] = False

print(count)

for k in no_overlaps.keys():
    if no_overlaps[k]:
        print(k)
