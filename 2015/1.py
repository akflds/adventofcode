#!/usr/bin/python3

with open('/mnt/c/Misc/2015-d1-input') as f:
    data = f.readline().rstrip()


def p1():
    floor = 0
    for c in data:
        if c == '(':
            floor += 1
        else:
            floor -= 1

    return floor

def p2():

    floor = 0
    pos = 1
    for c in data:
        if c == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return pos
        else:
            pos += 1
        
print(p1())
print(p2())

