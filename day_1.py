with open("day_1_input.txt") as f:
    ns = {int(l) for l in f.readlines()}


# part 1
for n in ns:
    diff = 2020 - n
    if diff in ns:
        print(diff * n)
        break


# part 2
from itertools import combinations

paired = {a + b: (a, b) for a, b in combinations(ns, 2)}

for n in ns:
    diff = 2020 - n
    if diff in paired:
        a, b = paired[diff]
        print(n * a * b)
        break
