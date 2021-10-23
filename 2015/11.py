#!/usr/bin/python3

from string import ascii_lowercase
import re

subs = [ascii_lowercase[i:i+3] for i in range (len(ascii_lowercase) -2)]

def straight(s):
    return any(c in s for c in subs)

def valid_chars(s):
    return not any(c in s for c in ['i', 'o', 'l']) 

def double_pairs(s):
    return bool(re.search(r'^.*(\w)\1.*(\w)\2.*$', s))

def increment(s):
    if s.endswith('z'):
        s = s[:-1] + 'a'
    else:
        s = s[:-1] + chr(ord(s[-1]) + 1)
    if s[-1] != 'a':
        return s
    else:
        return increment(s[:-1]) + 'a'

def get_new_pass(old):
    new = increment(old)
    while not straight(new) or not valid_chars(new) or not double_pairs(new):
        new = increment(new)
    return new

print(get_new_pass('REDACTED'))
print(get_new_pass(get_new_pass('REDACTED')))
