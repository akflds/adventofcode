#!/usr/bin/python3

with open('1.txt') as f:
        data = f.readline().strip()

def p1():
        total = 0
        digits = [int(x) for x in str(data)]
        for i in range(0, len(digits)):
                if i < len(digits) - 1 and digits[i] == digits[i+1]:
                        total += digits[i]
                elif  i == len(digits) - 1 and digits[i] == digits[0]:
                        total += digits[i]
        print(total)

def p2():
        total = 0
        digits = [int(x) for x in str(data)]
        mid = int(len(digits) / 2)
        
        for i, d in enumerate(digits):
                if d == digits[(i + mid) % len(digits)]:
                        total += d
                
        print(total)

p1()
p2()
