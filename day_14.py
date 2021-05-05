with open("day_14_input.txt") as f:
    s = f.read()

L = len("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
p = lambda x: print(f"{x:b}".zfill(L), x)
flip = lambda x: x ^ (2 ** L - 1)
ons = lambda mask, n: mask | n
offs = lambda mask, n: flip(mask | flip(n))

def yield_instructions(instructions):
    for instruction in instructions:
        _, rest = instruction.split("[")
        address, rest = rest.split("]")
        _, n = rest.split(" = ")
        yield int(address), int(n)

def yield_programs():
    for program in s.split("\nmask = "):
        m, *instructions = program.splitlines()
        yield m.replace("mask = ", ""), yield_instructions(instructions)

# part 1
memory = {}
for m, instructions in yield_programs():
    mask_ons = int(m.replace("X", "0"), 2)
    mask_offs = int(m.replace("1", "X").replace("0", "1").replace("X", "0"), 2)
    for address, n in instructions:
        memory[address] = offs(mask_offs, ons(mask_ons, n))

print(sum(memory.values()))

# part 2
memory = {}
for m, instructions in yield_programs():
    floaters = [2 ** i for i, c in enumerate(reversed(m)) if c == "X"]
    mask_ons = int(m.replace("X", "0"), 2)
    for address, n in instructions:
        addresses = [ons(mask_ons, address)]
        for floater in floaters:
            original = addresses[:]
            addresses = []
            for address in original:
                addresses.append(ons(floater, address))
                addresses.append(offs(floater, address))
        for address in addresses:
            memory[address] = n

print(sum(memory.values()))
