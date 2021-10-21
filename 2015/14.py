#!/usr/bin/python3

deers = dict()

with open('/home/andrew/Downloads/2015-d14-input', 'r') as f:
    for line in f:
        l = line.split()
        deers[l[0]] = {'speed': int(l[3]), 'duration': int(l[6]), 'rest': int(l[-2])}

def race(s):
    td = dict()
    for k, v in deers.items():
        d = (v['speed'] * v['duration']) * (s // (v['duration'] + v['rest']))
        remainder = s % (v['duration'] + v['rest'])
        if remainder - v['duration'] > 0:
            d += v['speed'] * v['duration']
        else:
            d += v['speed'] * remainder
        td[k] = d
    return(td)

print("Part 1:")
print(max(race(2503).values()))

lb = dict.fromkeys(deers.keys(), 0)
for i in range(1, 2503+1):
    rnd = race(i)
    high_dist = max(rnd.values())
    winners = [k for k, v in rnd.items() if v == high_dist]
    for w in winners:
        lb[w] += 1

print("Part 2:")
print(max(lb.values()))
