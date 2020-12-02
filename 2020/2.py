#!/usr/bin/python3

with open('/mnt/c/Misc/2020-d2-input') as f:
    data = f.readlines()


def p1():
    passwords = []

    for line in data:
        l = line.split()
        bounds = list(map(int, l[0].split('-')))
        letter = l[1].rstrip(':')
        password = l[2]
        
        if password.count(letter) in range(bounds[0], bounds[1]+1):
            passwords.append(password)

    return len(passwords)

def p2():
    passwords = []

    for line in data:
        l = line.split()
        positions = list(map(int,l[0].split('-')))
        letter = l[1].rstrip(':')
        password = l[2]
        
        to_check = [password[pos-1] for pos in positions]

        if to_check.count(letter) == 1:
            passwords.append(password)

    return len(passwords)

print(p1())
print(p2())
