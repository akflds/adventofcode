#!/usr/bin/python3

import math

with open('/mnt/c/Misc/2015-d2-input') as f:
    data = f.readlines()


def p1():
    paper = 0

    for line in data:
        l,w,h = [int(x) for x in line.rstrip().split('x')]
        area = [l*w, w*h, h*l]
        paper += sum([2*x for x in area]) + min(area)

    return paper

def p2():
    ribbon = 0

    for line in data:
        dims = [int(x) for x in line.rstrip().split('x')]
        ribbon += math.prod(dims)
        dims.remove(max(dims))
        ribbon += sum([2*x for x in dims])
    
    return ribbon
        
print(p1())
print(p2())

