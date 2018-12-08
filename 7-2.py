file = open("7-1.in", "r")
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
workers = 5
offset = 4
# file = open("7-1.in.test", "r")
# letters = list('ABCDEF')
# workers = 2
# offset = 64

steps = {x: [] for x in letters}
completed = {x: False for x in letters}
time = {x: 0 for x in letters}
running = []

for line in file:
    (_, pre, _, _, _, _, _, post, _, _) = line.strip().split()
    steps[post].append(pre)

string = ''
timer = 0
while False in completed.values():
    for_iteration = running.copy()
    for l in for_iteration:
        time[l] += 1
        if time[l] == ord(l) - offset:
            completed[l] = True
            string += l
            running.remove(l)

    if len(running) < workers:
        for l in letters:
            if not completed[l] and l not in running:
                ready = True
                for pre in steps[l]:
                    if not completed[pre]:
                        ready = False
                if ready and len(running) < workers:
                    running.append(l)

    timer += 1

print(timer-1)
