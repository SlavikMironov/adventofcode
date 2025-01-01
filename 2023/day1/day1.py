def get_puzzle(path):
    with open(path) as file:
        return file.read().split()


def part_one(puzzle: list[str]):
    first_num, second_num = None, None
    s = 0

    for puzzle_row in puzzle:
        for i in range(len(puzzle_row)):
            if puzzle_row[i].isdigit():
                first_num = puzzle_row[i]
                break

        for i in range(len(puzzle_row) - 1, -1, -1):
            if puzzle_row[i].isdigit():
                second_num = puzzle_row[i]
                break
        s += int(first_num + second_num)

    return s


def part_two(puzzle: list[str]):
    first_num, second_num = None, None
    s = 0
    numbers = [
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]

    for puzzle_row in puzzle:
        num_found = False

        for i in range(len(puzzle_row)):
            if num_found:
                break
            if puzzle_row[i].isdigit():
                first_num = puzzle_row[i]
                break
            else:
                for num in numbers:
                    digit, value = num

                    if i + len(digit) - 1 < len(puzzle_row):
                        if puzzle_row[i : i + len(digit)] == digit:
                            first_num = value
                            num_found = True
                            break
        num_found = False

        for i in range(len(puzzle_row) - 1, -1, -1):
            if num_found:
                break
            if puzzle_row[i].isdigit():
                second_num = puzzle_row[i]
                break
            else:
                for num in numbers:
                    digit, value = num

                    if i - len(digit) + 1 >= 0:
                        if puzzle_row[i - len(digit) + 1 : i + 1] == digit:
                            second_num = value
                            num_found = True
                            break
        s += int(first_num + second_num)

    return s


path = "input.txt"

puzzle = get_puzzle(path)

print(f"Part one: {part_one(puzzle)}")
print(f"Part two: {part_two(puzzle)}")
