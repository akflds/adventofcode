#!/usr/bin/python3

with open('/mnt/c/Misc/2020-d5-input', 'r') as f:
    data = f.read().split('\n')

def p1():
    seats = []
    for line in data:
        rows = list(range(128))
        cols = list(range(8))
        rw = line[:8]
        cl = line[-3:]
        for r in rw:
            if r == 'F':
                rows = rows[:len(rows)//2]
            else:
                rows = rows[len(rows)//2:]
        for c in cl:
            if c == 'L':
                cols = cols[:len(cols)//2]
            else:
                cols = cols[len(cols)//2:]
        
        seats.append(rows[0]*8 + cols[0])

    return seats

def p2(seats):
    all_ids = [i*8+j for i in range(128) for j in range(8)]
    diffs = set(all_ids) - set(seats)
    for d in diffs:
        if d+1 in seats and d-1 in seats:
            return d

print(max(p1()))

print(p2(p1()))

