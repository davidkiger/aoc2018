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
    regs[c] = int(regs[a] & regs[b])
    return regs


def bani(regs, a, b, c):
    regs[c] = int(regs[a] & b)
    return regs


def borr(regs, a, b, c):
    regs[c] = int(regs[a] | regs[b])
    return regs


def bori(regs, a, b, c):
    regs[c] = int(regs[a] | b)
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

solved_codes = {
    0: set(),
    1: set(),
    2: set(),
    3: set(),
    4: set(),
    5: set(),
    6: set(),
    7: set(),
    8: set(),
    9: set(),
    10: set(),
    11: set(),
    12: set(),
    13: set(),
    14: set(),
    15: set(),
}
lines = file.readlines()
real_regs = [0, 0, 0, 0]
for i in range(len(lines)):
    if i < 3260:
        if lines[i].startswith('Before: '):
            match = 0
            _, pre_str = lines[i].split(': ')
            pre = [int(x) for x in pre_str.replace('[', '').replace(']', '').strip().split(', ')]

            _, post_str = lines[i+2].split(': ')
            post = [int(x) for x in post_str.replace('[', '').replace(']', '').strip().split(', ')]

            inst = [int(x) for x in lines[i+1].split()]

            codes = []
            if addr(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('addr')
            if addi(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('addi')
            if mulr(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('mulr')
            if muli(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('muli')
            if banr(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('banr')
            if bani(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('bani')
            if borr(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('borr')
            if bori(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('bori')
            if setr(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('setr')
            if seti(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('seti')
            if gtir(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('gtir')
            if gtri(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('gtri')
            if gtrr(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('gtrr')
            if eqir(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('eqir')
            if eqri(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('eqri')
            if eqrr(pre[:], inst[1], inst[2], inst[3]) == post:
                match += 1
                codes.append('eqrr')

            i += 3
            solved_codes[inst[0]].update(codes)
    elif i == 3260:
        keep_going = True
        while keep_going:
            for code, ops in solved_codes.items():
                if len(ops) == 1:
                    for code2, ops2 in solved_codes.items():
                        if code2 != code:
                            try:
                                ops2.remove(list(ops)[0])
                            except:
                                pass

            keep_going = False
            for k, v in solved_codes.items():
                if len(v) > 1:
                    keep_going = True

        for k, v in solved_codes.items():
            solved_codes[k] = list(v)
        i += 1
    else:
        inst = [int(x) for x in lines[i].split()]
        if len(inst) == 4:
            real_regs = locals()[solved_codes[inst[0]][0]](real_regs, inst[1], inst[2], inst[3])
            i += 1

print(real_regs[0])
