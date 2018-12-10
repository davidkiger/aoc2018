file = open("10-1.in", "r")

stars = []
for line in file:
    x = int(line[10:16])
    y = int(line[17:24])
    x_v = int(line[-8:-6])
    y_v = int(line[-5:-2])

    stars.append({'p': [x, y], 'v': [x_v, y_v]})

t = 0
while True:
    t += 1
    max_height = 0

    for star in stars:
        star['p'][0] += star['v'][0]
        star['p'][1] += star['v'][1]

    coords = [z['p'] for z in stars]
    ys = [z['p'][1] for z in stars]

    max_height = abs(max(ys) - min(ys))
    if max_height < 10:
        xs = [z['p'][0] for z in stars]
        max_width = abs(max(xs) - min(xs))

        for y in range(min(ys), max(ys)+1):
            string = ''
            for x in range(min(xs), max(xs)+1):
                if [x, y] in coords:
                    string += '#'
                else:
                    string += '.'
            print(string)
        print(t)
        exit()
