#!/usr/bin/python3

with open('/mnt/c/Misc/2020-d6-input', 'r') as f:
    data = f.read().strip().split('\n\n')

def p1():
    qs = 0

    for group in data:
        group = group.replace('\n', '')
        qs += len(set(group))
                    
    return qs

def p2():
    allans = 0
    for group in data:
        ans = {}
        
        for answers in group.split('\n'):
            for a in answers:
                ans[a] = ans.get(a, 0) + 1
        
        allans += sum(x == len(group.split('\n')) for x in ans.values())
        
    return allans

print(p1())

print(p2())

