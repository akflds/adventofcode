#!/usr/bin/python3

from hashlib import md5


def p(inp, zeros):
    i = 0
    while True:
        h = md5((inp+str(i)).encode()).hexdigest()
        if h[:zeros] == '0' * zeros:
            return i
        else:
            i += 1

print(p('yzbqklnj',5))
print(p('yzbqklnj',6))
