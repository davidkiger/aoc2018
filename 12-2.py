from copy import deepcopy

file = open("12-1.in", "r")

rules = {}
for line in file:
    if line[0] == 'i':
        init = line.strip()[15:]
    elif line.strip():
        i, _, o = line.strip().split()
        rules[i] = o

state = {i: x for i, x in enumerate(list(init))}
for i in range(-10, 0):
    state[i] = '.'
for i in range(100, 2000):
    state[i] = '.'

for gen in range(1000):
    new_state = deepcopy(state)
    for pos in state.keys():
        comp = state.get(pos-2, '.')
        comp += state.get(pos-1, '.')
        comp += state[pos]
        comp += state.get(pos+1, '.')
        comp += state.get(pos+2, '.')

        if comp in rules:
            new_state[pos] = rules[comp]
        else:
            new_state[pos] = state[pos]

    string = ''.join(str(x) for x in [new_state[k] for k in sorted(new_state.keys())])
    state = new_state

string = ''.join(str(x) for x in [state[k] for k in sorted(state.keys())])
sum_pots = 0
for x in state.keys():
    if state[x] == '#':
        sum_pots += int(x)

# From prior output, I knew my diff at this stage was 63
print((50000000000 - 1000) * 63 + sum_pots)
