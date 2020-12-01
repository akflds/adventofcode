#!/usr/bin/python3

with open('input') as f:
    expenses = f.readlines()

entries = [int(expense) for expense in expenses]

n = len(entries)

for i in range(n):
    for j in range (i, n):
        if entries[i] + entries[j] == 2020:
            print("Part 1: ", entries[i]*entries[j]) 

        for k in range (j, n):
            if entries[i] + entries[j] + entries[k] == 2020:
                print("Part 2: ", entries[i]*entries[j]*entries[k]) 
