import re
from copy import deepcopy

match = re.compile('(\d+)\D+(\d+)[^(]+(\(.+\))?\D+(\d+)\s(\S+)\s\D+(\d+)')

file = open("24-1.in", "r")

o_groups = []

lines = file.readlines()
inf_g = 0
imm_g = 0
for i, line in enumerate(lines):
    l = match.match(line)
    if not l or len(l.groups()) < 5:
        continue

    weak = []
    imm = []
    if l.group(3):
        parse = l.group(3).replace(')', '').replace('(', '').split('; ')
        for p in parse:
            if p[0] == 'w':
                weak.extend(p[8:].split(', '))
            elif p[0] == 'i':
                imm.extend(p[10:].split(', '))

    if i < 11:
        group_type = 'immune'
        imm_g += 1
        group_id = 'imm' + str(imm_g)
        boost = 1
    else:
        group_type = 'infect'
        inf_g += 1
        group_id = 'inf' + str(inf_g)
        boost = 0

    o_groups.append({
        'group_id': group_id,
        'group_type': group_type,
        'units': int(l.group(1)),
        'hp': int(l.group(2)),
        'weak': weak,
        'immune': imm,
        'damage': int(l.group(4)),
        'type': l.group(5),
        'initiative': int(l.group(6)),
        'boost': boost
    })

groups = deepcopy(o_groups)
boost = 1

while True:
    prev_imm = prev_inf = 0
    while True:
        targets = []
        groups = sorted(groups, key=lambda x: (x['units'] * (x['damage'] + x['boost']), x['initiative']), reverse=True)
        chosen = []
        for a, attacker in enumerate(groups):
            target_id = -1
            projected_damage = 0
            target_ep = 0
            target_init = 0
            power = attacker['units'] * (attacker['damage'] + attacker['boost'])
            for d, defender in enumerate(groups):
                if defender['group_id'] in chosen or attacker['group_type'] == defender['group_type']:
                    continue

                potential_damage = power
                if attacker['type'] in defender['immune']:
                    continue
                elif attacker['type'] in defender['weak']:
                    potential_damage *= 2

                if potential_damage > projected_damage:
                    target_id = defender['group_id']
                    target_ep = defender['units'] * (defender['damage'] + defender['boost'])
                    target_init = defender['initiative']
                    projected_damage = potential_damage
                elif potential_damage == projected_damage:
                    if (defender['units'] * (defender['damage'] + defender['boost'])) > target_ep or (defender['units'] * defender['damage'] == target_ep and defender['initiative'] > target_init):
                        target_id = defender['group_id']
                        target_ep = defender['units'] * (defender['damage'] + defender['boost'])
                        target_init = defender['initiative']

            if target_id != -1:
                targets.append([attacker['group_id'], target_id, attacker['initiative']])
                chosen.append(target_id)

        stalemate = True
        targets = sorted(targets, key=lambda x: x[2], reverse=True)
        for target in targets:
            attacker = [a for a in groups if a['group_id'] == target[0]][0]
            defender = [d for d in groups if d['group_id'] == target[1]][0]

            damage = attacker['units'] * (attacker['damage'] + attacker['boost'])
            if attacker['type'] in defender['weak']:
                damage *= 2
            elif attacker['type'] in defender['immune']:
                damage = 0

            units_killed = damage // defender['hp']
            defender['units'] = max(0, defender['units'] - units_killed)
            if units_killed > 0:
                stalemate = False

        groups = [g for g in groups if g['units'] > 0]
        count_inf = len([g for g in groups if g['group_type'] == 'infect'])
        count_imm = len([g for g in groups if g['group_type'] == 'immune'])

        if count_inf == 0:
            units = 0
            for g in groups:
                units += g['units']
            print(units)
            exit()

        if count_imm == 0 or stalemate:
            break

    boost += 1
    groups = deepcopy(o_groups)
    for g in groups:
        if g['group_type'] == 'immune':
            g['boost'] = boost
