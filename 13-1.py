file = open("13-1.in", "r")

carts = []
paths = []
y = 0
for line in file:
    path = line
    for p, c in enumerate(path):
        if c == '<':
            carts.append({'x': p, 'y': y, 'c': c, 't': 0})
        if c == '>':
            carts.append({'x': p, 'y': y, 'c': c, 't': 0})
        if c == '^':
            carts.append({'x': p, 'y': y, 'c': c, 't': 0})
        if c == 'v':
            carts.append({'x': p, 'y': y, 'c': c, 't': 0})

    path = path.replace('<', '-').replace('>', '-').replace('v', '|').replace('^', '|')
    paths.append(list(path))
    y += 1

while True:
    for cart in carts:
        check = paths[cart['y']][cart['x']]

        if check == '/':
            if cart['c'] == '>':
                cart['c'] = '^'
            elif cart['c'] == '<':
                cart['c'] = 'v'
            elif cart['c'] == 'v':
                cart['c'] = '<'
            elif cart['c'] == '^':
                cart['c'] = '>'
        elif check == '\\':
            if cart['c'] == '>':
                cart['c'] = 'v'
            elif cart['c'] == '<':
                cart['c'] = '^'
            elif cart['c'] == 'v':
                cart['c'] = '>'
            elif cart['c'] == '^':
                cart['c'] = '<'
        elif check == '+':
            if cart['t'] == 0:
                # Turn left
                if cart['c'] == '>':
                    cart['c'] = '^'
                elif cart['c'] == '<':
                    cart['c'] = 'v'
                elif cart['c'] == 'v':
                    cart['c'] = '>'
                elif cart['c'] == '^':
                    cart['c'] = '<'
            elif cart['t'] == 1:
                pass
            elif cart['t'] == 2:
                # Turn right
                if cart['c'] == '>':
                    cart['c'] = 'v'
                elif cart['c'] == '<':
                    cart['c'] = '^'
                elif cart['c'] == 'v':
                    cart['c'] = '<'
                elif cart['c'] == '^':
                    cart['c'] = '>'

            cart['t'] += 1
            cart['t'] %= 3

        if cart['c'] == '>':
            cart['x'] += 1
        elif cart['c'] == '<':
            cart['x'] -= 1
        elif cart['c'] == 'v':
            cart['y'] += 1
        elif cart['c'] == '^':
            cart['y'] -= 1

        for c2 in carts:
            if cart == c2:
                pass
            elif cart['x'] == c2['x'] and cart['y'] == c2['y']:
                print('{} {}'.format(cart['x'], cart['y']))
                exit()
