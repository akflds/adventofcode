#!/usr/bin/python3

from collections import defaultdict
from itertools import permutations

distances = defaultdict(dict) # avoid key errors

with open('/home/andrew/Downloads/2015-d9-input', 'r') as f:
    for line in f:
        source, _, destination, _, distance = line.split()
        distances[source][destination] = int(distance)
        distances[destination][source] = int(distance)

# get list of all places
places = set(x for x in distances.keys())

lengths = []

# permutations() creates all possible journeys
for perm in permutations(places):
    # adds up distances between each pair in the permutation 
    lengths.append(sum(map(lambda x, y: distances[x][y], perm[:-1], perm[1:])))

print("Part 1:")
print(min(lengths))
print("Part 2:")
print(max(lengths))
