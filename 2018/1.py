#!/usr/bin/python3

with open('/mnt/c/Misc/2018-d1-input') as f:
    data = f.readlines()

x = [int(change.rstrip()) for change in data]

def p1():
    f = 0
    for i in x:
        f += i
      
    return(f)

def p2():
    f = 0
    frequencies = set ()
    frequencies.add(f)
    
    while True:
        for i in x:
            f += i
            if f not in frequencies:
                frequencies.add(f)
            else:
                return(f)

print(p1())
print(p2())
