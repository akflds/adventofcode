#!/usr/bin/python3

from hashlib import md5


def p1(inp):
    i = 0
    while True:
        h = md5((inp+str(i)).encode()).hexdigest()
        if h[:6] == '000000':
            return i
        else:
            i += 1

print(p1('yzbqklnj'))
