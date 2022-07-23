#!/usr/bin/python3

with open('4.txt') as f:
    phrases = f.readlines()

total = 0
secure_total = 0

for phrase in phrases:
  words = phrase.strip().split(" ")
  if len(words) == len(set(words)):
    total += 1
  words = [" ".join(sorted(w)) for w in words]
  if len(words) == len(set(words)):
    secure_total += 1
  
print(total)
print(secure_total)