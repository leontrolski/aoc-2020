from collections import defaultdict
from itertools import count

s = open("day_19_input.txt").read()
add_to_stack = ()
final_state = (1, ())
rules, examples = s.split("\n\n")
r = {}
for rule in rules.splitlines():
    n, tail = rule.split(": ")
    n = int(n)
    r[n] = frozenset(
        tuple(int(m) if m.isdigit() else m[1:-1] for m in ands.split())
        for ands in tail.split("|")
    )


# part 2
r[8] = frozenset(((42, ), (42, 8)))
r[11] = frozenset(((42, 31), (42, 11, 31)))


def make_state_machine(rules, starting_rule):
    js = count(1)
    d = defaultdict(set)

    def make(rule, x, y, scope):
        if isinstance(rule, (frozenset, tuple)) and len(rule) == 1:
            rule = next(iter(rule))  # optimisation

        if isinstance(rule, int):
            if rule in scope:
                _x, _y = scope[rule]
                d[x].add((add_to_stack, _x))
                d[_y].add((_x, y))
            else:
                make(rules[rule], x, y, {rule: (x, y), **scope})
        elif isinstance(rule, frozenset):  # or
            for m in rule:
                i, j = next(js), next(js)
                d[x].add((None, i))
                d[j].add((None, y))
                make(m, i, j, scope)
        elif isinstance(rule, tuple):  # and
            middles = [next(js) for _ in range(len(rule) - 1)]
            froms_tos = zip(rule, [x, *middles], [*middles, y])
            for m, i, j in froms_tos:
                make(m, i, j, scope)
        else:  # letter
            d[x].add((rule, y))

    make(rules[starting_rule], 0, next(js), {0: (0, 1)})
    return d

state_machine = make_state_machine(r, 0)

def next_possible_states(state, only_edges):
    return {next_state for edge, next_state in state_machine[state] if edge == only_edges}

def test(e):
    states = {(0, ())}

    def transition(a, b, stack, add=False, pop=False):
        states.discard((a, stack))
        states.add((b, stack[:-1] if pop else stack + (b,) if add else stack))

    i = 0
    for _ in range(len(e) + 1):
        while True:  # traverse all epsilon|add_to_stack|pop_stack edges
            original_states = set(states)
            for a, stack in original_states - {final_state}:
                for b in next_possible_states(a, None):
                    transition(a, b, stack)
                for b in next_possible_states(a, add_to_stack):
                    transition(a, b, stack, add=True)
                if stack:
                    for b in next_possible_states(a, stack[-1]):
                        transition(a, b, stack, pop=True)
            if states == original_states:
                break

        if states != {final_state} and i < len(e):  # traverse letter edges
            states = {(b, stack) for a, stack in states for b in next_possible_states(a, e[i])}
            i += 1

        if not states:
            return False
        if final_state in states:
            return i == len(e)

    return False

print(sum(test(e) for e in examples.splitlines()))
