from functools import cmp_to_key


def get_puzzle(path):
    puzzle = []

    with open(path) as file:
        for pairs in file.read().split("\n\n"):
            first_list, second_list = pairs.splitlines()
            puzzle.append((eval(first_list), eval(second_list)))

    return puzzle


def part_two(puzzle):
    puzzles = []
    for l, r in puzzle:
        puzzles.append(l)
        puzzles.append(r)
    puzzles.extend([[[2]], [[6]]])
    sorted_packets = sorted(puzzles, key=cmp_to_key(compare_part_two))

    index_2 = sorted_packets.index([[2]]) + 1
    index_6 = sorted_packets.index([[6]]) + 1

    return index_2 * index_6


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
        return None

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            result = compare(l, r)
            if result is not None:
                return result
        return len(left) < len(right) if len(left) != len(right) else None

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    return compare(left, right)


def compare_part_two(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else (1 if left > right else 0)

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            result = compare_part_two(l, r)
            if result != 0:
                return result
        return -1 if len(left) < len(right) else (1 if len(left) > len(right) else 0)

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    return compare_part_two(left, right)


def part_one(puzzle):
    s = 0

    def compare(left, right):
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            if left > right:
                return False
            return None

        if isinstance(left, list) and isinstance(right, list):
            for l, r in zip(left, right):
                result = compare(l, r)
                if result is not None:
                    return result
            return len(left) < len(right) if len(left) != len(right) else None

        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]

        return compare(left, right)

    for index, (left_list, right_list) in enumerate(puzzle):
        if compare(left_list, right_list):
            s += index + 1

    return s


path = "input.txt"

puzzle = get_puzzle(path)
print(f"Part one: {part_one(puzzle)}")
print(f"Part two: {part_two(puzzle)}")
