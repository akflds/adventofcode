#!/usr/bin/python3

def init_lights():
    with open('/home/andrew/Downloads/2015-d18-input', 'r') as f:
        lights = [list(line.strip()) for line in f]
    return lights
    
def get_lit(x, y, l):
    total = 0
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1),
                   ( 0, -1),          ( 0, 1),
                   ( 1, -1), ( 1, 0), ( 1, 1)]:
        try:
            if x+dx >= 0 and y+dy >= 0 and l[x+dx][y+dy] == '#':
                total += 1
        except IndexError:
            pass
    return total

lights = init_lights()
for step in range(100):
    new_lights = []

    for x in range(100):
        l = []
        for y in range(100):
            # 4x conditionals for p2 corner lights
            if x == 0 and y == 0:
                l.append('#')
            elif x == 0 and y == 99:
                l.append('#')
            elif x == 99 and y == 0:
                l.append('#')
            elif x == 99 and y == 99:
                l.append('#')
            else:
                nb = get_lit(x, y, lights)
                if lights[x][y] == '#' and nb in [2,3]:
                    l.append('#')
                elif lights[x][y] == '.' and nb == 3:
                    l.append('#')
                else:
                    l.append('.')

        new_lights.append(l)
    lights = deepcopy(new_lights)

total = 0
for x in range(100):
    for y in range(100):
        if lights[x][y] == '#':
            total += 1

print(total)

