file = open("7-1.in", "r")
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

steps = {x: [] for x in letters}
completed = {x: False for x in letters}

for line in file:
    (_, pre, _, _, _, _, _, post, _, _) = line.strip().split()
    steps[post].append(pre)

string = ''
while False in completed.values():
    first_pass = True
    for l in letters:
        if not completed[l] and first_pass:
            ready = True
            for pre in steps[l]:
                if not completed[pre]:
                    ready = False
            if ready:
                first_pass = False
                completed[l] = True
                string += l

print(string)
