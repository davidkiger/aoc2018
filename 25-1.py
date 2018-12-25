from collections import deque
file = open("25-1.in", "r")

points = []
for line in file:
    points.append([int(x) for x in line.strip().split(',')])

used = []
constellations = []

for point in points:
    if point not in used:
        test_queue = deque([point])
        this_constellation = []
        while test_queue:
            test = test_queue.pop()
            if test not in this_constellation:
                this_constellation.append(test)
                used.append(test)
                for p in points:
                    if p == test:
                        continue

                    dist = abs(p[0] - test[0]) + abs(p[1] - test[1]) + abs(p[2] - test[2]) + abs(p[3] - test[3])
                    if dist <= 3:
                        test_queue.append(p)

        constellations.append(this_constellation)

print(len(constellations))
