with open("day_11_input.txt") as f:
    s = f.read()

# part 2
rows = [list(line) for line in s.splitlines() if line]
h, w = len(rows), len(rows[0])
legit = {"#", "L"}

for _ in range(200000):
    out = [row[:] for row in rows]
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            if v == ".":
                continue
            d = range(i - 1, -1, -1)
            u = range(i + 1, h)
            l = range(j - 1, -1, -1)
            r = range(j + 1, w)
            tangents = (
                (rows[x][j] for x in d),
                (rows[x][j] for x in u),
                (rows[i][y] for y in l),
                (rows[i][y] for y in r),
                (rows[x][y] for x, y in zip(u, l)),
                (rows[x][y] for x, y in zip(u, r)),
                (rows[x][y] for x, y in zip(d, l)),
                (rows[x][y] for x, y in zip(d, r)),
            )
            neighbours = []
            for tangent in tangents:
                for n in tangent:
                    if n in legit:
                        neighbours.append(n)
                        break

            if v == "L" and "#" not in neighbours:
                out[i][j] = "#"
            elif v == "#" and len([n for n in neighbours if n == "#"]) >= 5:
                out[i][j] = "L"
    if out == rows:
        print(len([v for row in rows for v in row if v == "#"]))
        break
    rows = out

# print("\n".join(["".join(row) for row in out]))

