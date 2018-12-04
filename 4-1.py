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

sorted_sleeps = sorted(sleeps.items(), key=lambda x: x[1]['total'])
print(sorted_sleeps[-1])
sorteds = sorted(sorted_sleeps[-1][1]['mins'].items(), key=lambda x: x[1])
print(sorteds[-1])

print(int(sorted_sleeps[-1][0]) * int(sorteds[-1][0]))
