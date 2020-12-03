#!/usr/bin/python3

with open('/mnt/c/Misc/2020-d3-input') as f:
    data = f.readlines()


def p1(start):
    forest = [line.rstrip() for line in data]
    trees = 0
    cell = start[1]
    for line in range(start[0], len(forest), start[0]):
        if forest[line][cell % len(forest[line])] == '#':
            trees += 1
        cell += start[1]
            
    return trees


def p2():
    trees = p1([1,1]) * p1([1,3]) * p1([1,5]) * p1([1,7]) * p1([2,1])
    return trees

print(p1([1,3]))
print(p2())

