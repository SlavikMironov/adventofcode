def get_puzzle(path):
    pairs = []

    with open(path) as file:
        for line in file.read().splitlines():
            pairs.append(
                tuple(
                    tuple(int(bound) for bound in p.split("-")) for p in line.split(",")
                )
            )

        return pairs


def part_one(puzzle):
    return sum(
        (p2[0] <= p1[0] <= p2[1] and p2[0] <= p1[1] <= p2[1])
        or (p1[0] <= p2[0] <= p1[1] and p1[0] <= p2[1] <= p1[1])
        for p1, p2 in puzzle
    )


def part_two(puzzle):
    return sum((p1[1] >= p2[0] and p1[0] <= p2[1]) for p1, p2 in puzzle)


path = "input.txt"

puzzle = get_puzzle(path)
print(f"Part one: {part_one(puzzle)}")
print(f"Part two: {part_two(puzzle)}")
