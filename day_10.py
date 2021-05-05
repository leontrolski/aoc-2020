with open("day_10_input.txt") as f:
    ns = [int(line) for line in f.readlines()]

ns = sorted(ns)

# part 1
diffs = [b - a for a, b in zip(ns, ns[1:])]
_1s = len([d for d in diffs if d == 1]) + 1
_3s = len([d for d in diffs if d == 3]) + 1
print(_1s * _3s)

# part 2
d = {ns.pop(): 1}
for n in list(reversed(ns)) + [0]:
    d[n] = d.get(n+1, 0) + d.get(n+2, 0) + d.get(n+3, 0)

print(d[0])
