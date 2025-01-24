def get_puzzle(path):
    with open(path) as file:
        return file.read()


def part_one(puzzle):
    for i in range(len(puzzle) - 4):
        if len(set(puzzle[i : i + 4])) == 4:
            return i + 4


def part_two(puzzle):
    for i in range(len(puzzle) - 14):
        if len(set(puzzle[i : i + 14])) == 14:
            return i + 14


path = "input.txt"
puzzle = get_puzzle(path)
print(f"Part one: {part_one(puzzle)}")
print(f"Part two: {part_two(puzzle)}")
