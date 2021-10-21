#!/usr/bin/python3

from collections import defaultdict
from itertools import permutations

pairs = defaultdict(dict) # avoid key errors

with open('/home/andrew/Downloads/2015-d13-input', 'r') as f:
    for line in f:
        x, _, sign, happiness, _, _, _, _, _, _, y = line.replace('.','').split()
        if sign == "gain":
            pairs[x][y] = int(happiness)
        else:
            pairs[x][y] = int(happiness) * -1

guests = set(x for x in pairs.keys())

def get_scores(g):
    scores = list()
    for perm in permutations(g):
        # adds up distances between each pair in the permutation 
        s = list(map(lambda x, y: pairs[x][y] + pairs[y][x], perm[:-1], perm[1:]))
        s.append(pairs[perm[-1]][perm[0]] + pairs[perm[0]][perm[-1]])
        scores.append(sum(s))
    return scores

print("Part 1:")
print(max(get_scores(guests)))

for guest in guests:
    pairs[guest]['me'] = pairs['me'][guest] = 0

guests.add('me')

print("Part 2:")
print(max(get_scores(guests)))


