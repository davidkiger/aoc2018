file = open("17-1.in", "r")

ground = [['.' for i in range(1000)] for j in range(1680)]
ground[0][500] = '+'
pos = [[500, 0]]
min_y = 500
for line in file:
    if line[0] == 'x':
        x_, y_ = line.strip().split(', ')
        _, x = x_.split('=')
        x = int(x)
        _, y = y_.split('=')
        ys = y.split('..')
        if int(ys[0]) < min_y:
            min_y = int(ys[0])
        for y in range(int(ys[0]), int(ys[1])+1):
            ground[y][x] = '#'
    elif line[0] == 'y':
        y_, x_ = line.strip().split(', ')
        _, y = y_.split('=')
        y = int(y)
        if y < min_y:
            min_y = y
        _, x = x_.split('=')
        xs = x.split('..')
        for x in range(int(xs[0]), int(xs[1])+1):
            ground[y][x] = '#'

count = 0
while len(pos):
    count += 1
    new_pos = []
    for k, p in enumerate(pos):
        x = p[0]
        y = p[1]
        try:
            c = ground[y+1][x]
            if c == '#' or c == '~':
                this_left = x-1
                while this_left > 0 and ground[y][this_left] != '#':
                    this_left -= 1

                this_right = x+1
                while this_right < (len(ground[y])-1) and ground[y][this_right] != '#':
                    this_right += 1

                if c == '~':
                    next_left = x-1
                    while next_left > 0 and ground[y+1][next_left] != '#':
                        next_left -= 1
                    next_right = x+1
                    while next_right < (len(ground[y+1])-1) and ground[y+1][next_right] != '#':
                        next_right += 1
                else:
                    next_left = x-1
                    while next_left > 0 and ground[y+1][next_left] == '#':
                        next_left -= 1
                    next_right = x+1
                    while next_right < (len(ground[y+1])-1) and ground[y+1][next_right] == '#':
                        next_right += 1
                    next_left += 1
                    next_right -= 1

                in_bucket = True
                for t in range(this_left, this_right+1):
                    if ground[y+1][t] != '~' and ground[y+1][t] != '#':
                        in_bucket = False

                if in_bucket:
                    for t in range(this_left+1, this_right):
                        ground[y][t] = '~'
                    p[1] -= 1
                else:
                    for t in range(next_left, next_right+1):
                        if ground[y][t] != '#':
                            ground[y][t] = '|'
                    if ground[y][next_left] != '#':
                        ground[y][next_left-1] = '|'
                        new_pos.append([next_left-1, y])
                    if ground[y][next_right] != '#':
                        ground[y][next_right+1] = '|'
                        new_pos.append([next_right+1, y])
                    pos[k] = [-1, -1]
            elif c == '.':
                ground[y+1][x] = '|'
                p[1] += 1
            elif c == '|':
                pos[k] = [-1, -1]
        except:
            pos[k] = [-1, -1]

    pos = [q for q in pos if q[0] != -1]
    pos.extend(new_pos)

tilde = 0
pipe = 0
for j in range(min_y, 1680):
    # print(''.join(ground[j]))
    tilde += ground[j].count('~')

print(tilde)
