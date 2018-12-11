grid = [[0 for i in range(300)] for j in range(300)]

def calc(x, y):
    serial = 1309
    rack = x + 10
    pl = (((rack * (rack * y + serial)) // 100) % 10) - 5
    return(pl)

for y, row in enumerate(grid):
    for x, el in enumerate(row):
        grid[x][y] = calc(x, y)

max_sum = -1000000
coords = ''
for i in range(1, 301):
    for y, row in enumerate(grid):
        for x, el in enumerate(row):
            this_sum = 0
            try:
                this_sum = grid[x][y]
                for j in range(i):
                    for k in range(i):
                        this_sum += grid[x+j][y+k]

                if this_sum > max_sum:
                    max_sum = this_sum
                    coords = '{},{},{}'.format(x, y, i)
                    print(coords)

            except:
                pass

print(coords)
