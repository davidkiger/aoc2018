file = open("1-1.in", "r")

freq = 0
for line in file:
    sign = line.strip()[0]
    num = int(line.strip()[1:])
    if sign == '+':
        freq += num
    else:
        freq -= num

print(freq)
