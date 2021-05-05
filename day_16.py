from functools import reduce, partial
from math import prod

with open("day_16_input.txt") as f:
    s = f.read()

# parse input
rules_, me, nearby = s.split("\n\n")
all_rules = {}
for line in rules_.splitlines():
    name, a_bs = line.split(":")
    a_bs = [r.split("-") for r in a_bs.split("or")]
    a_bs = [(int(a), int(b)) for a, b in a_bs]
    all_rules[name] = [partial(lambda a, b, n: a <= n <= b, a, b) for a, b in a_bs]
me = [int(a) for a in me.splitlines()[1].split(",")]
nearby = [line.split(",") for line in nearby.splitlines()[1:]]
nearby = [tuple(int(n) for n in split) for split in nearby]

# part 1
rules = [rule for rules in all_rules.values() for rule in rules]
total = 0
for ticket in nearby:
    for n in ticket:
        if not any(rule(n) for rule in rules):
            total += n

print(total)

# part 2
all_passes = []
for ticket in nearby:
    passes = []
    for n in ticket:
        names = {name for name, rules in all_rules.items() if any(rule(n) for rule in rules)}
        passes.append(names)
    if all(passes):
        all_passes.append(passes)

done = [None] * len(all_rules)
while None in done:
    for i, col in enumerate(zip(*all_passes)):
        intersection = reduce(lambda a, b: a & b, col) - set(done)
        if len(intersection) == 1:
            done[i], = intersection

total = prod(n for name, n in zip(done, me) if name.startswith("departure"))
print(total)
