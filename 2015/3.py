#!/usr/bin/python3

import math

with open('/mnt/c/Misc/2015-d3-input') as f:
    data = f.readline().rstrip()


def p1():
    x = y = 0
    houses = {(0,0)}
    for d in data:
        if d == '>':
            x += 1
        elif d == '<':
            x -= 1
        elif d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        houses.add((x,y))

    return len(houses)

def move(d, x, y):
    if d == '>':
        x += 1
    elif d == '<':
        x -= 1
    elif d == '^':
        y += 1
    elif d == 'v':
        y -= 1
    return x,y

def p2():
    sx = sy = rx = ry = 0
    houses = {(0,0)}
    santa = True
    
    for d in data:
        if santa:
            sx, sy = move(d, sx, sy)
            houses.add((sx,sy))
        else:
            rx, ry = move(d, rx, ry)
            houses.add((rx,ry))
        santa = not santa
        
    return len(houses)

        
print(p1())
print(p2())

