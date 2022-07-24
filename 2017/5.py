#!/usr/bin/python3

with open('5.txt') as f:
    lines = f.readlines()
    data = [int(x) for x in lines]

def p1(d):
  steps = 0
  i = 0
  while i < len(d):
    jump = d[i]
    d[i] += 1
    i = i + jump
    steps += 1
    if i >= len(d):
      print(steps)

def p2(d):
  steps = 0
  i = 0
  while i < len(d):
    jump = d[i]
    if jump >= 3:
      d[i] -= 1
    else:
      d[i] += 1
    i = i + jump
    steps += 1
    if i >= len(d):
      print(steps)

p1(data.copy())
p2(data.copy())

