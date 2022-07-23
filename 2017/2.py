#!/usr/bin/python3

with open('2.txt') as f:
    data = f.readlines()

total = 0
div_total = 0

for d in data:
  d = [int(x) for x in d.strip().split("\t")]
  total += max(d)-min(d)
  d.sort(reverse=True)
  for i in range(0, len(d)):
    for j in range(i + 1, len(d)):
      if d[i] % d[j] == 0:
        div_total += int(d[i] / d[j])
  
print("p1:", total)
print("p2:", div_total)