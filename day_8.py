with open("day_8_input.txt") as f:
    lines = list(f.readlines())

def run(swap_i):
    acc = 0
    i = 0
    ran = set()
    while i < len(lines):
        if i in ran:
            return None
        ran.add(i)
        instruction, num = lines[i].split(" ")
        num = int(num)

        if i == swap_i:
            if instruction == "jmp":
                instruction = "nop"
            elif instruction == "nop":
                instruction = "jmp"

        if instruction == "nop":
            i += 1
        elif instruction == "jmp":
            i += num
        elif instruction == "acc":
            i += 1
            acc += num
    return acc

for i in range(len(lines)):
    acc = run(i)
    if acc is not None:
        print(acc)
        break
