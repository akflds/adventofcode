#!/usr/bin/python3

import itertools

containers = []

with open('/home/andrew/Downloads/2015-d17-input', 'r') as f:
    for line in f:
        containers.append(int(line.strip()))

total = 0
m = 0
for i in range(1, len(containers)+1):
    for x in itertools.combinations(containers, i):
        if sum(x) == 150:
            total += 1
    # first valid combos of containers will have lowest length
    if total and not m:
        m = total

print("Part 1:")
print(total)
print("Part 2:")
print(m)

