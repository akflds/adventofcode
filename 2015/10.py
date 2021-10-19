#!/usr/bin/python3

from itertools import groupby

inp = "" # redacted!

def game(s, rounds):
    for i in range(rounds):
        groups = [''.join(g) for _, g in groupby(s)]
        s = ''
        for g in groups:
            s += str(len(g)) + str(g[0])
    return len(s)

print(game(inp, 40))
print(game(inp, 50))


