def get_puzzle(path):
    with open(path) as file:
        return file.read().splitlines()


def part_one(cmds):
    cycle = 1
    x = 1
    s = 0

    for cmd in cmds:
        if cycle % 40 == 20:
            s += x * cycle

        if cmd == "noop":
            cycle += 1
        else:
            if cycle % 40 == 19:
                s += x * (cycle + 1)
            x += int(cmd.split()[-1])
            cycle += 2

    return s


def part_two(cmds):
    cycle = 1
    x = 1
    crt = [["."] * 40 for _ in range(6)]

    for cmd in cmds:
        i, j = (cycle - 1) // 40, ((cycle - 1) % 40)
        if x - 1 <= j <= x + 1:
            crt[i][j] = "#"

        if cmd == "noop":
            cycle += 1
        else:
            i, j = cycle // 40, cycle % 40
            if x - 1 <= j <= x + 1:
                crt[i][j] = "#"

            x += int(cmd.split()[-1])
            cycle += 2
    for row in crt:
        print("".join(row))


path = "input.txt"
cmds = get_puzzle(path)
print(f"Part one: {part_one(cmds)}")
part_two(cmds)
