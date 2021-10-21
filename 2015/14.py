#!/usr/bin/python3

deers = dict()
s = 2503

with open('/home/andrew/Downloads/2015-d14-input', 'r') as f:
    for line in f:
        l = line.split()
        deers[l[0]] = {'speed': int(l[3]), 'duration': int(l[6]), 'rest': int(l[-2])}

distances = list()
for k, v in deers.items():
    d = (v['speed'] * v['duration']) * (s // (v['duration'] + v['rest']))
    remainder = s % (v['duration'] + v['rest'])
    if remainder - v['duration'] > 0:
        d += v['speed'] * v['duration']
    else:
        d += v['speed'] * remainder
    distances.append(d)

print("Part 1:")
print(max(distances))

