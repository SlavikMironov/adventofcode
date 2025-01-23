def get_input(path):
    puzzle = []

    with open(path) as file:
        for s in file.read().split("\n\n"):
            puzzle.append(sum(map(int, s.split())))
    return puzzle


def part_one(puzzle):
    return max(puzzle)


def part_two(puzzle):
    m1 = m2 = m3 = -1

    for num in puzzle:
        if num > m1:
            m1, m2, m3 = num, m1, m2
        elif num > m2:
            m2, m3 = num, m2
        elif num > m3:
            m3 = num

    return sum((m1, m2, m3))


path = "input.txt"

puzzle = get_input(path)
print(f"Part one: {part_one(puzzle)}")
print(f"Part two: {part_two(puzzle)}")
