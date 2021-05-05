s = open("day_12_input.txt").read()

m = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
fs = list(m)

# part 1
f = "E"
x, y = 0, 0
for line in s.splitlines():
    instruction = line[0]
    n = int(line[1:])

    if instruction in {"R", "L"}:
        if instruction == "L":
            n = -n
        n = int(n / 90)
        f = fs[(fs.index(f) + n) % 4]
        continue

    if instruction == "F":
        instruction = f
    _x, _y = m[instruction]
    x += _x * n
    y += _y * n

print(abs(x) + abs(y))

# part 2
x, y = 0, 0
i, j = 10, 1
for line in s.splitlines():
    instruction = line[0]
    n = int(line[1:])

    if instruction == "F":
        x += i * n
        y += j * n
    elif instruction in {"R", "L"}:
        if instruction == "L":
            n = -n
        n = int(n % 360 / 90)
        for _ in range(n):
            o = i
            i += -o + j
            j += -o - j
    else:
        _x, _y = m[instruction]
        i += _x * n
        j += _y * n

print(abs(x) + abs(y))
