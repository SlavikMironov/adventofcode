import re


def get_puzzle(path):
    with open(path) as file:
        pattern = r"move (\d+) from (\d+) to (\d+)"
        stacks_str, moves_str = file.read().split("\n\n")
        stacks_str = stacks_str.splitlines()
        stacks = [[] for _ in range(int(stacks_str[-1][-2]))]
        moves = []

        for s in stacks_str[-2::-1]:
            for i in range(1, len(s), 4):
                if s[i] != " ":
                    stacks[i // 4].append(s[i])

        for move in moves_str.splitlines():
            groups = re.findall(pattern, move)
            moves.append(
                (int(groups[0][0]), int(groups[0][1]) - 1, int(groups[0][2]) - 1)
            )

        return stacks, moves


def part_one(stacks, moves):
    for amount, first_stack, second_stack in moves:
        n = len(stacks[first_stack]) - amount
        stacks[second_stack].extend(stacks[first_stack][n:][::-1])
        stacks[first_stack] = stacks[first_stack][:n]
    return "".join(s[-1] for s in stacks)


def part_two(stacks, moves):
    for amount, first_stack, second_stack in moves:
        n = len(stacks[first_stack]) - amount
        stacks[second_stack].extend(stacks[first_stack][n:])
        stacks[first_stack] = stacks[first_stack][:n]
    return "".join(s[-1] for s in stacks)


path = "input.txt"

stacks, moves = get_puzzle(path)
print(f"Part one: {part_one(stacks, moves)}")
stacks, moves = get_puzzle(path)
print(f"Part two: {part_two(stacks, moves)}")
