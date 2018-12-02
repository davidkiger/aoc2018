file = open("2-1.in", "r")

count_2 = 0
count_3 = 0
for line in file:
    chars = line.strip()
    char_map = {}
    for c in chars:
        if c in char_map:
            char_map[c] += 1
        else:
            char_map[c] = 1

    if 2 in char_map.values():
        count_2 += 1
    if 3 in char_map.values():
        count_3 += 1

print(count_2 * count_3)
