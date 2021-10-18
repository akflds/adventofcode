#!/usr/bin/python3

with open('/home/andrew/Downloads/2015-d6-input', 'r') as f:
    data = [line.strip().replace('turn ', '').replace('through ', '').split() for line in f]


def init_lights():
    return [[0 for i in range(1000)] for j in range(1000)]

def illuminate(actions):
    lights = init_lights()
    for line in data:
        action = line[0]
        x1, y1 = map(int, line[1].split(","))
        x2, y2 = map(int, line[2].split(","))
        coords = [(x, y) for x in range(x1, x2+1) for y in range(y1, y2+1)]
        for x, y in coords:
            lights[x][y] = actions[action](lights[x][y])

    return sum(sum(light) for light in lights)

def p1():

    actions = {
            "on": lambda x: 1,
            "off": lambda x: 0,
            "toggle": lambda x: 1 if x == 0 else 0
            }
    return illuminate(actions)

def p2():
    actions = {
            "on": lambda x: x + 1,
            "off": lambda x: x - 1 if x > 0 else 0,
            "toggle": lambda x: x + 2
            }
    return illuminate(actions)

print(p1())
print(p2())
