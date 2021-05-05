ss = open("day_18_input.txt").read().splitlines()
op_map = {"*": lambda a, b: a * b, "+": lambda a, b: a + b}  # from low to high precedence

def tokenise(s):
    s = s.replace(" ", "")
    acc = []
    for c in s + "\n":
        if c.isdigit():
            acc.append(c)
        else:
            if acc:
                yield int("".join(acc))
            if c != "\n":
                yield c
            acc = []

def nest(tokens):
    acc = []
    for t in tokens:
        if t == ")":
            return acc
        elif t == "(":
            acc.append(nest(tokens))
        else:
            acc.append(t)
    return acc

def parse(l):
    if not isinstance(l, list):
        return l
    if len(l) == 1:
        return parse(l[0])
    a, op, b, *tail = l
    v = op_map[op](parse(a), parse(b))
    return parse([v] + tail)

print(sum(parse(nest(tokenise(s))) for s in ss))

def parse(l):
    if not isinstance(l, list):
        return l
    if len(l) == 1:
        return parse(l[0])
    for op, f in op_map.items():
        split = next((i for i, n in enumerate(l) if n == op), None)
        if split is not None:
            head, tail = l[:split], l[split + 1:]
            return f(parse(head), parse(tail))

print(sum(parse(nest(tokenise(s))) for s in ss))


assert list(tokenise("1 + (4 + (5 + 6 + 77)) + 88")) == [1, '+', '(', 4, '+', '(', 5, '+', 6, '+', 77, ')', ')', '+', 88]
assert list(tokenise("(1+ 5)")) == ['(', 1, "+", 5, ")"]

assert nest(tokenise("1 + (4 + (5 + 6 + 77)) + 88")) == [1, '+', [4, '+', [5, '+', 6, '+', 77]], '+', 88]
assert nest(tokenise("(1+ 5)")) == [[1, "+", 5]]
