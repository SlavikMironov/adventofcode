commands = []

for line in open("input.txt").read().splitlines():
    cmd, val = line.split()
    commands.append([cmd, int(val)])
change_val = {"nop": "jmp", "jmp": "nop"}
n = len(commands)


def get_acc(program):
    seen = set()
    accumulator = 0
    i = 0
    while i < n:
        if i in seen:
            return True, accumulator
        seen.add(i)
        cmd, val = program[i]

        if cmd == "jmp":
            i += val
        else:
            if cmd == "acc":
                accumulator += val
            i += 1
    return False, accumulator


print(f"Part one: {get_acc(commands)[1]}")

for i in range(n):
    if commands[i][0] in change_val:
        key = commands[i][0]
        commands[i][0] = change_val[key]
        cycle, acc = get_acc(commands)
        if not cycle:
            print(f"Part two: {acc}")
            break
        commands[i][0] = key
