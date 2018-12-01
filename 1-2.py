file = open("1-1.in", "r")

freq = 0
freqs = {}
while(True):
    for line in file:
        sign = line.strip()[0]
        num = int(line.strip()[1:])
        if sign == '+':
            freq += num
        else:
            freq -= num

        if freq in freqs:
            print(freq)
            exit()
        else:
            freqs[freq] = True

    file = open("1-1.in", "r")
