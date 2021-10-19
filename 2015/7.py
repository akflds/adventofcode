#!/usr/bin/python3

import functools

# input and output dicts
instructions = {}
wires = {}

with open('/home/andrew/Downloads/2015-d7-input', 'r') as f:
    for line in f:
        # split instruction into two and assign to dict
        x, y = line.split(' -> ')
        instructions[y.strip()] = x.split(' ')

def assemble(wire):
    try:
        return int(wire)
    except ValueError:
        pass
    
    if wire not in wires:
        instruction = instructions[wire]
        # valid operators = AND, OR, NOT, RSHIFT, LSHIFT
        if 'AND' in instruction:
            value = assemble(instruction[0]) & assemble(instruction[2])
        elif 'OR' in instruction:
            value = assemble(instruction[0]) | assemble(instruction[2])
        elif 'NOT' in instruction:
            value = ~assemble(instruction[1]) & 0xffff
        elif 'RSHIFT' in instruction:
            value = assemble(instruction[0]) >> assemble(instruction[2])
        elif 'LSHIFT' in instruction:
            value = assemble(instruction[0]) << assemble(instruction[2])
        else: # assume assignment
            value = assemble(instruction[0])
        wires[wire] = value
    return wires[wire]

# part 1
print("Part 1:")
print(assemble('a'))
print("Part 2:")
instructions['b'] = [str(assemble('a'))]
wires.clear()
print(assemble('a'))
