file = open("16-1.in", "r")


def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]
    return regs


def addi(regs, a, b, c):
    regs[c] = regs[a] + b
    return regs


def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]
    return regs


def muli(regs, a, b, c):
    regs[c] = regs[a] * b
    return regs


def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]
    return regs


def bani(regs, a, b, c):
    regs[c] = regs[a] & b
    return regs


def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]
    return regs


def bori(regs, a, b, c):
    regs[c] = regs[a] | b
    return regs


def setr(regs, a, b, c):
    regs[c] = regs[a]
    return regs


def seti(regs, a, b, c):
    regs[c] = a
    return regs


def gtir(regs, a, b, c):
    regs[c] = int(a > regs[b])
    return regs


def gtri(regs, a, b, c):
    regs[c] = int(regs[a] > b)
    return regs


def gtrr(regs, a, b, c):
    regs[c] = int(regs[a] > regs[b])
    return regs


def eqir(regs, a, b, c):
    regs[c] = int(a == regs[b])
    return regs


def eqri(regs, a, b, c):
    regs[c] = int(regs[a] == b)
    return regs


def eqrr(regs, a, b, c):
    regs[c] = int(regs[a] == regs[b])
    return regs


lines = file.readlines()
mtt = 0
for i in range(len(lines)):
    if lines[i].startswith('Before: '):
        match = 0
        _, pre_str = lines[i].split(': ')
        pre = [int(x) for x in pre_str.replace('[', '').replace(']', '').strip().split(', ')]

        _, post_str = lines[i+2].split(': ')
        post = [int(x) for x in post_str.replace('[', '').replace(']', '').strip().split(', ')]

        inst = [int(x) for x in lines[i+1].split()]

        if addr(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if addi(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if mulr(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if muli(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if banr(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if bani(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if borr(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if bori(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if setr(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if seti(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if gtir(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if gtri(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if gtrr(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if eqir(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if eqri(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1
        if eqrr(pre[:], inst[1], inst[2], inst[3]) == post:
            match += 1

        if match >= 3:
            mtt += 1

        i += 3

print(mtt)
