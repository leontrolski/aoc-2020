from itertools import combinations

with open("day_9_input.txt") as f:
    ns = [int(line) for line in f.readlines()]

# part 1
l = 25
for i in range(l, len(ns)):
    possible = {a + b for a, b in combinations(ns[i - l: i], 2)}
    x = ns[i]
    if x not in possible:
        target = x
        print(target)
        break

# part 2
for contig in range(1, 50):
    for i, n in enumerate(ns):
        if i + contig > len(ns):
            continue
        r = ns[i:i + contig]
        if n != target and sum(r) == target:
            print(min(r) + max(r))
