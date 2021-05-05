from functools import lru_cache, reduce
from itertools import product
s = """
...#...#
..##.#.#
###..#..
........
...##.#.
.#.####.
...####.
..##...#
""".strip()

N = 3
offsets = set(product(*[[-1, 0, 1]] * N)) - {tuple([0] * N)}

@lru_cache(None)
def get_neighbours(coords):
    return {tuple(coords[i] + offset[i] for i in range(N)) for offset in offsets}

g = {
    (x, y, *[0] * (N - 2))
    for y, line in enumerate(s.splitlines())
    for x, char in enumerate(line)
    if char == "#"
}
for t in range(6):
    empty_neighbours = reduce(lambda a, b: a | b, (get_neighbours(coords) for coords in g)) - g
    new =  {coords for coords in g if                len(g & get_neighbours(coords)) in {2, 3}}
    new |= {coords for coords in empty_neighbours if len(g & get_neighbours(coords)) in {3}}
    g = new

print(len(g))







# helper for part 1
to_char = {True: "#", False: "."}

def pp(g):
    xs, ys, zs = zip(*g)
    x_range = range(min(xs), max(xs) + 1)
    y_range = range(min(ys), max(ys) + 1)
    z_range = range(min(zs), max(zs) + 1)
    for z in z_range:
        print(f"z={z}")
        for y in y_range:
            print("".join(to_char[(x, y, z) in g] for x in x_range))
        print()
