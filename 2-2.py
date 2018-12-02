file = open("2-1.in", "r")

lines = []
for line in file:
    lines.append(line.strip())

for line in lines:
    for l2 in lines:
        if line == l2:
            continue

        diff = 0
        for i in range(len(l2)):
            if l2[i] != line[i]:
                diff += 1

        if diff == 1:
            print(line)
            print(l2)
