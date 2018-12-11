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
for y, row in enumerate(grid):
    for x, el in enumerate(row):
        try:
            this_sum  = grid[x][y] + grid[x+1][y] + grid[x+2][y]
            this_sum += grid[x][y+1] + grid[x+1][y+1] + grid[x+2][y+1]
            this_sum += grid[x][y+2] + grid[x+1][y+2] + grid[x+2][y+2]

            if this_sum > max_sum:
                max_sum = this_sum
                coords = '{},{}'.format(x, y)
        except:
            pass

print(coords)
