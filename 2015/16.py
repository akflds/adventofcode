#!/usr/bin/python3

results = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
        }

sues = dict()

with open('/home/andrew/Downloads/2015-d16-input', 'r') as f:
    for line in f:
        l = line.replace(',', '').replace(':', '').split()
        prop = {
                l[2]: int(l[3]),
                l[4]: int(l[5]),
                l[6]: int(l[7])
                }
        sues[l[1]] = prop

print("Part 1:")
for sue, props in sues.items():
    if props.items() <= results.items():
        print(sue)

print("Part 2:")
for sue, props in sues.items():
    matches = []
    for k, v in props.items():
        if k in ['cats', 'trees']:
            matches.append(results[k] < v)
        elif k in ['pomeranians', 'goldfish']:
            matches.append(results[k] > v)
        else:
            matches.append(results[k] == v)
    if all(matches):
        print(sue)
