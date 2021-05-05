from pathlib import Path

s = (Path(__file__).parent / "day_6_input.txt").read_text()

# part 1
print(sum(len(set(group.replace("\n", ""))) for group in s.split("\n\n")))

# part 2
total = 0
for group in s.split("\n\n"):
    people = set(frozenset(p) for p in group.strip().split("\n"))
    letters = people.pop()
    for person in people:
        letters &= person
    total += len(letters)

print(total)
