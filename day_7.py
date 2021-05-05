m = {}
with open("day_7_input.txt") as f:
    for line in f.readlines():
        colour, tail = line.replace("bags", "").replace("bag", "").replace(".", "").split("contain")
        colour = colour.strip()
        tail = [n.strip() for n in tail.split(",")]
        if tail == ["no other"]:
            tail = []
        m[colour] = {child: int(count) for count, _, child in (n.partition(" ") for n in tail)}

# part 1
def yield_children(colour):
    for child in m[colour]:
        yield child
        yield from yield_children(child)

gold_parents = 0
for colour in m:
    gold_parents += "shiny gold" in set(yield_children(colour))
print(gold_parents)

# part 2
def get_count(colour):
    return sum(count * (get_count(child) + 1) for child, count in m[colour].items())

print(get_count("shiny gold"))
