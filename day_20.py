from copy import deepcopy
from collections import defaultdict
from itertools import product
from math import prod

with open("day_20_input.txt") as f:
    s = f.read()
L = len("..##.#..#.")
p = lambda x: print(f"{x:b}".zfill(L), x)
to_int = lambda x: int(x.replace("#", "1").replace(".", "0"), 2)

test = 1
if test:
    s = """Tile 2311:
    ..##.#..#.
    ##..#.....
    #...##..#.
    ####.#...#
    ##.##.###.
    ##...#.###
    .#.#.#..##
    ..#....#..
    ###...#.#.
    ..###..###

    Tile 1951:
    #.##...##.
    #.####...#
    .....#..##
    #...######
    .##.#....#
    .###.#####
    ###.##.##.
    .###....#.
    ..#.#..#.#
    #...##.#..

    Tile 1171:
    ####...##.
    #..##.#..#
    ##.#..#.#.
    .###.####.
    ..###.####
    .##....##.
    .#...####.
    #.##.####.
    ####..#...
    .....##...

    Tile 1427:
    ###.##.#..
    .#..#.##..
    .#.##.#..#
    #.#.#.##.#
    ....#...##
    ...##..##.
    ...#.#####
    .#.####.#.
    ..#..###.#
    ..##.#..#.

    Tile 1489:
    ##.#.#....
    ..##...#..
    .##..##...
    ..#...#...
    #####...#.
    #..#.#.#.#
    ...#.#.#..
    ##.#...##.
    ..##.##.##
    ###.##.#..

    Tile 2473:
    #....####.
    #..#.##...
    #.##..#...
    ######.#.#
    .#...#.#.#
    .#########
    .###.#..#.
    ########.#
    ##...##.#.
    ..###.#.#.

    Tile 2971:
    ..#.#....#
    #...###...
    #.#.###...
    ##.##..#..
    .#####..##
    .#..####.#
    #..#.#..#.
    ..####.###
    ..#.#.###.
    ...#.#.#.#

    Tile 2729:
    ...#.#.#.#
    ####.#....
    ..#.#.....
    ....#..#.#
    .##..##.#.
    .#.####...
    ####.#.#..
    ##.####...
    ##..#.##..
    #.##...##.

    Tile 3079:
    #.#.#####.
    .#..######
    ..#.......
    ######....
    ####.#..#.
    .#...#.##.
    #.#####.##
    ..#.###...
    ..#.......
    ..#.###...
    """

def yield_variations(rows):
    for _rows in (  # flip both ways
        [row for row in rows],
        ["".join(reversed(row)) for row in rows],
        list(reversed(rows)),
    ):
        for _ in range(4):
            _rows = zip(*reversed(_rows))  # rotate 90 degrees
            _rows = ["".join(r) for r in _rows]
            yield _rows

tiles = {}
candidates = defaultdict(set)
sides_to_specifics = {}
for tile in s.split("\n\n"):
    if not tile:
        continue
    _, n, *rows = tile.split()
    n = int(n[:-1])
    tiles[n] = set()
    sides_to_specifics[n] = {}
    for rows in yield_variations(rows):
        rows = ["".join(r) for r in rows]
        cols = ["".join(c) for c in zip(*rows)]
        t = to_int(rows[0])
        l = to_int(cols[0])
        b = to_int(rows[-1])
        r = to_int(cols[-1])
        sides = t, l, b, r
        tiles[n].add(sides)
        candidates[n] |= set(sides)
        sides_to_specifics[n][sides] = "\n".join(rows)

def possible_neighbours(n, side):
    return {_n for _n, sides in candidates.items() if _n != n and side in sides}

def neighbour(i, j, tlbr, edge_tlbrs):
    n, sides = grid[i][j]
    neighbours = {
        (_n, _sides)
        for _n in possible_neighbours(n, sides[tlbr])
        for _sides in tiles[_n]
        if sides[tlbr] == _sides[(tlbr + 2) % 4]
        and not any(possible_neighbours(_n, _sides[e]) for e in edge_tlbrs)
    }
    assert len(neighbours) == 1, f"saw {neighbours}"
    [n, sides], = neighbours
    return n, sides

def top_left():
    for n, sidess in tiles.items():
        for sides in sidess:
            if not (possible_neighbours(n, sides[0]) | possible_neighbours(n, sides[1])):
                return n, sides

def pop(i, j):
    n, _ = grid[i][j]
    tiles.pop(n), candidates.pop(n)
    print(grid)


w = int(len(tiles) ** 0.5)
grid = [[None for _ in range(w)] for _ in range(w)]

grid[0][0] = top_left()
pop(0, 0)
grid[0][1] = neighbour(0, 0, 3, {0})
pop(0, 1)
grid[0][2] = neighbour(0, 1, 3, {0, 3})
pop(0, 2)

grid[1][2] = neighbour(0, 2, 2, {3})
pop(1, 2)
grid[2][2] = neighbour(1, 2, 2, {3})
pop(1, 2)


grid[1][0] = neighbour(0, 0, 2, {1})
pop(1, 0)
grid[2][0] = neighbour(1, 0, 2, {1, 2})
pop(2, 0)





print(grid)




#         for tlbr in range(4):
#             if not matches[tlbr]:
#                 return EDGE

# CORNER, EDGE = "CORNER", "EDGE"
# def get_type(n):
#     for sides in tiles[n]:
#         matches = [bool(set(possible_neighbours(n, sides[tlbr]))) for tlbr in range(4)]
#         for tlbr in range(4):
#             if not matches[tlbr] and not matches[(tlbr + 1) % 4]:
#                 return CORNER
#         for tlbr in range(4):
#             if not matches[tlbr]:
#                 return EDGE


# corner_tiles = {n for n in tiles if get_type(n) == CORNER}
# edge_tiles = {n for n in tiles if get_type(n) == EDGE}
# print(prod(corner_tiles))


# w = int(len(tiles) ** 0.5)
# isjs = list(product(range(w), range(w)))
# corner_isjs = ((0, 0), (w - 1, 0), (0, w - 1), (w - 1, w - 1))
# all_possibilities_lte = lambda grid, n: all(all(sum(len(sidess) for sidess in grid[i][j].values()) <= n for j in range(w)) for i in range(w))

# def yield_valid_sides(n, sidess, grid, neighbours):
#     for sides in sidess:
#         matching = sum(
#             any(
#                 sides[(_tlbr + 2) % 4] == _sides[_tlbr]
#                 for _n, _sidess in grid[_i][_j].items()
#                 for _sides in _sidess
#                 if n != _n
#             )
#             for _i, _j, _tlbr in neighbours
#         )
#         if matching == len(neighbours):
#             yield sides

# def solve():
#     grid = [[None for _ in range(w)] for _ in range(w)]
#     for i, j in isjs:
#         grid[i][j] = {
#             n: set(sidess) for n, sidess in tiles.items()
#             if not (
#                 ((i, j) in corner_isjs and n not in corner_tiles) and
#                 ((i in {0, w - 1} or j in {0, w - 1}) and n not in edge_tiles)
#             )
#         }

#     # print([sum(len(sidess) for sidess in grid[i][j].values() for j in range(w)) for i in range(w)])

#     for t in range(100):
#         next_grid = [[defaultdict(set) for _ in range(w)] for _ in range(w)]
#         for i, j in isjs:
#             neighbours = [(i  + _i, j + _j, _tlbr) for _i, _j, _tlbr in ((1, 0, 0), (0, 1, 1), (-1, 0, 2), (0, -1, 3))]
#             neighbours = [(_i, _j, _tlbr) for _i, _j, _tlbr in neighbours if 0 <= _i < w and 0 <= _j < w]
#             for n, sidess in grid[i][j].items():
#                 for valid_sides in yield_valid_sides(n, sidess, grid, neighbours):
#                     next_grid[i][j][n].add(valid_sides)

#         if all_possibilities_lte(next_grid, 1):
#             return [[next(iter(n)) for n in row] for row in grid]

#         if next_grid == grid:
#             # temporary
#             first = set(next_grid[0][0])
#             grid = [[None for _ in range(w)] for _ in range(w)]
#             for i, j in corner_isjs:
#                 grid[i][j] = first.pop()
#             return grid

#             # if not all_possibilities_lte(next_grid, 8):
#             #     raise RuntimeError
#             # for i, j in isjs:
#             #     if len(next_grid[i][j]) != 1:
#             #         next_grid[i][j].pop(next(iter(next_grid[i][j])))
#             #         break

#         grid = next_grid

# solved = solve()
# print(solved)
# print(prod(solved[i][j] for i, j in corner_isjs))
