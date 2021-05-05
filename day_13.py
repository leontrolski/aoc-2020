s = open("day_12_input.txt").read()

s="""1000391
19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,383,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,457,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17
"""

# part 1
t, _, bs = s.partition("\n")
t = int(t)
bs = [int(b) for b in bs.split(",") if b != "x"]
diffs = [-t % b for b in bs]
print(min(diffs) * bs[diffs.index(min(diffs))])

# part 2
_, _, bs = s.partition("\n")
bs = [(int(b), i) for i, b in enumerate(bs.split(",")) if b != "x"]
b, i = bs.pop()
for c, j in bs:
    t = -i
    while (t + j) % c:
        t += b
    b *= c
    i = b - t

print(t)
