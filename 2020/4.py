#!/usr/bin/python3

import re

with open('/mnt/c/Misc/2020-d4-input') as f:
    data = f.readlines()


def p1():
    pwd = {}
    pwds = []

    for line in data:
        line = line.rstrip().split()
        if line:
            pwd.update(dict([x.split(':') for x in line]))
        else:
            pwds.append(pwd)
            pwd = {}

    valid = []

    for pw in pwds:
        if len(pw.keys()) == 8:
            valid.append(pw)
        elif len(pw) == 7 and 'cid' not in pw:
            valid.append(pw)

    return valid


def p2(pwds):
    valid = 0
    for pw in pwds:
        if 1920 <= int(pw['byr']) <= 2002:
            if 2010 <= int(pw['iyr']) <= 2020:
                    if 2020 <= int(pw['eyr']) <=2030:
                        if (pw['hgt'][-2:] == 'cm' and 150 <= int(pw['hgt'][:-2]) <= 193) or (pw['hgt'][-2:] == 'in' and 59 <= int(pw['hgt'][:-2]) <= 76):
                            if re.fullmatch('^#[0-9a-f]{6}$', pw['hcl']):
                                if pw['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                    if re.fullmatch('^[0-9]{9}$', pw['pid']):
                                        valid += 1
                                        
    return valid



print(len(p1()))

print(p2(p1()))

