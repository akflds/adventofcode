#!/usr/bin/python3
import re

ingredients = []

with open("15.txt", "r") as f:
    for line in f:
        _, props = line.strip().split(": ")
        ingredients.append(list(map(int, re.sub(
            r"[a-z\ ]*", "", props
        ).split(","))))

scores = []
low_calorie_scores = []

for i in range(0, 100):
  for j in range(0, 100-i):
    for k in range(0, 100-i-j):
      l = 100-i-j-k
      t_calories = max(0, ingredients[0][4] * i + ingredients[1][4] * j + ingredients[2][4] * k + ingredients[3][4] * l)
      t_capacity = max(0, ingredients[0][0] * i + ingredients[1][0] * j + ingredients[2][0] * k + ingredients[3][0] * l)
      t_durability = max(0, ingredients[0][1] * i + ingredients[1][1] * j + ingredients[2][1] * k + ingredients[3][1] * l)
      t_flavor = max(0, ingredients[0][2] * i + ingredients[1][2] * j + ingredients[2][2] * k + ingredients[3][2] * l)
      t_texture = max(0, ingredients[0][3] * i + ingredients[1][3] * j + ingredients[2][3] * k + ingredients[3][3] * l)
      if t_calories == 500:
        low_calorie_scores.append(t_capacity * t_durability * t_flavor * t_texture)
      scores.append(t_capacity * t_durability * t_flavor * t_texture)

print(max(scores))
print(max(low_calorie_scores))