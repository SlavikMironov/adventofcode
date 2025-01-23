def get_puzzle(path):
    with open(path) as file:
        return file.read().splitlines()


def part_one(puzzle):
    count = 0

    for p in puzzle:
        n = len(p) // 2
        item = (set(p[:n]) & set(p[n:])).pop()
        if item.islower():
            count += ord(item) - ord("a") + 1
        else:
            count += ord(item) - ord("A") + 27

    return count


def part_two(puzzle):
    count = 0

    for i in range(0, len(puzzle), 3):
        item = set(puzzle[i])
        for j in range(i + 1, i + 3):
            item &= set(puzzle[j])

        item = item.pop()
        if item.islower():
            count += ord(item) - ord("a") + 1
        else:
            count += ord(item) - ord("A") + 27

    return count


path = "input.txt"
puzzle = get_puzzle(path)
print(f"Part one: {part_one(puzzle)}")
print(f"Part two: {part_two(puzzle)}")
