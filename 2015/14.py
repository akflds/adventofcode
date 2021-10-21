#!/usr/bin/python3

deers = dict()

with open('/home/andrew/Downloads/2015-d14-input', 'r') as f:
    for line in f:
        l = line.split()
        deers[l[0]] = {'v': int(l[3]), 'd': int(l[6]), 'r': int(l[-2])}

def race(s):
    td = dict()
    for k, v in deers.items():
        # divmod returns quotient + remainder
        q, r = divmod(s, v['d'] + v['r'])
        # calculate the total travelling time * velocity
        td[k] = (q * v['d'] + min(r, v['d'])) * v['v']
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
