file = open("4-1.in.sorted", "r")

sleeps = {}
for line in file:
    tokens = line.strip().replace('[', '').replace(']', '').replace('#', '').split()
    date = tokens[0]
    time = tokens[1]
    string = ' '.join(tokens[2:])

    if tokens[-1] == 'shift':
        start = None
        guard = tokens[3]

    if tokens[2] == 'falls':
        (_, start) = time.split(':')
        if guard not in sleeps:
            sleeps[guard] = {'total': 0, 'mins': {}}

    if tokens[2] == 'wakes':
        (_, end) = time.split(':')
        sleeps[guard]['total'] += (int(end)-int(start))
        for i in range(int(start), int(end)):
            if i not in sleeps[guard]['mins']:
                sleeps[guard]['mins'][i] = 0
            sleeps[guard]['mins'][i] += 1

m = 0
for g, s in sleeps.items():
    sorteds = sorted(s['mins'].items(), key=lambda x: x[1])
    # print('{} {}'.format(g, sorteds))
    if sorteds[-1][1] > m:
        m = sorteds[-1][1]
        val = int(sorteds[-1][0]) * int(g)

print(val)
