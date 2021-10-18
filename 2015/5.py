#!/usr/bin/python3

import re

with open('/home/andrew/Downloads/2015-d5-input', 'r') as f:
    data = [line.strip() for line in f]

def count_vowels(s):
    return len(re.findall(r'[aeiou]', s))

def banned_pairs(s):
    return re.search(r'ab|cd|pq|xy', s) 

def double_chars(s):
    return re.search(r'(.)\1', s)

def p1():
    return len([line for line in data 
        if count_vowels(line) >= 3 
        and double_chars(line) 
        and not banned_pairs(line)])

def p2():
    return len([line for line in data 
        # match repeating letters with one letter between e.g. xyx
        if (re.search(r'(.).\1', line)) 
        # repeated pairs of letters that appear twice but do not overlap e.g. xyaxy
        and re.search(r'(..).*\1', line)])

print(p1())
print(p2())

