#!/usr/bin/python3

with open('/mnt/c/Misc/2018-d2-input') as f:
    data = f.readlines()


def p1():

    twos = 0
    threes = 0
    
    for x in data:
        freq = {}
        for i in x.rstrip():
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        if 2 in freq.values():
            twos += 1
        if 3 in freq.values():
            threes +=1 

    return twos*threes

def p2():
    for x in range(len(data)):
        for y in range(x+1, len(data)):
            diff_count = 0;
            diff_pos = 0;
            for i in range(len(data[x])):
                if data[x][i] != data[y][i]:
                    diff_count +=1
                    diff_pos = i

            if diff_count == 1:
                return data[x][:diff_pos] + data[x][diff_pos +  1:]

print(p1())
print(p2())
