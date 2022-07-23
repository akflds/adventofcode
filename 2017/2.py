#!/usr/bin/python3

with open('2.txt') as f:
    data = f.readlines()

total = 0

for d in data:
  d = [int(x) for x in d.strip().split("\t")]
  total += max(d)-min(d)

print(total)