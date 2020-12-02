#!/usr/bin/python3


with open('/mnt/c/Misc/2017-d1-input') as f:
        data = f.readline()

def p1():
        d = str(data)
        e = [int(x) for x in d]
        print(e)

def p2():
    return True

print(p1())
print(p2())
