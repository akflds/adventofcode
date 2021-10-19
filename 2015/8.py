#!/usr/bin/python3

import re

with open('/home/andrew/Downloads/2015-d8-input', 'r') as f:
    lines = [line.strip() for line in f]

p1 = 0
p2 = 0

for line in lines:
    p1 += len(line) - len(eval(line))
    # very lazy! +2 for quotes
    p2 += len(line.replace('\\', '\\\\').replace('"', '\\"')) - len(line) + 2

print(p1)
print(p2)
