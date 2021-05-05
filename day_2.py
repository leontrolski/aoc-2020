valid_1 = 0
valid_2 = 0
with open("day_2_input.txt") as f:
    for line in f.readlines():
        spec, example = line.split(":")  # 1-3 a: abcde
        example = example.strip()
        a_b, letter = spec.split(" ")
        a, b = a_b.split("-")
        a, b = int(a), int(b)
        valid_1 += a <= example.count(letter) <= b
        valid_2 += sum([example[a-1] == letter, example[b-1] == letter]) == 1

print(valid_1)
print(valid_2)
