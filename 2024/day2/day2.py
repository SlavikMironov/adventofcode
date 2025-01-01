def get_matrix(path):
    with open(path, "r") as file:
        return [list(map(int, line.split())) for line in file]


def part_one(matrix):
    return sum(check_increase(row) or check_decrease(row) for row in matrix)


def check_increase(row):
    return all(1 <= b - a <= 3 for a, b in zip(row[:-1], row[1:]))


def check_decrease(row):
    return all(1 <= a - b <= 3 for a, b in zip(row[:-1], row[1:]))


def check_part2_increase(row):
    for i in range(len(row) - 1):  # O(n)
        if not (1 <= row[i + 1] - row[i] <= 3):
            return check_increase(row[:i] + row[i + 1 :]) or check_increase(
                row[: i + 1] + row[i + 2 :]
            )


def check_part2_decrease(row):
    for i in range(len(row) - 1):  # O(n)
        if not (1 <= row[i] - row[i + 1] <= 3):
            return check_decrease(row[:i] + row[i + 1 :]) or check_decrease(
                row[: i + 1] + row[i + 2 :]
            )


def part_two(matrix):
    return sum(
        (
            check_increase(row)
            or check_part2_increase(row)
            or check_decrease(row)
            or check_part2_decrease(row)
        )  # O(n)
        for row in matrix
    )


def part_two_naive(matrix):
    return sum(
        (
            check_increase(row)
            or check_decrease(row)
            or any(
                check_increase(row[:i] + row[i + 1 :])
                or check_decrease(row[:i] + row[i + 1 :])
                for i in range(len(row))
            )
        )
        for row in matrix
    )


path = "input.txt"


matrix = get_matrix(path)

print(f"Part one {part_one(matrix)}")
print(f"Part two {part_two(matrix)}")
