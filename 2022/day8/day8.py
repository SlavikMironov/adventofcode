from collections import defaultdict


class coordinate:
    def __init__(self):
        self.left_max = None
        self.right_max = None
        self.up_max = None
        self.down_max = None


def get_puzzle(path):
    with open(path) as file:
        return [list(map(int, line)) for line in file.read().splitlines()]


def part_two(puzzle):
    n = len(puzzle)
    max_score = 0

    for row in range(n):
        for col in range(n):
            height = puzzle[row][col]
            left = right = up = down = 0

            for left_col in range(col - 1, -1, -1):
                left += 1
                if puzzle[row][left_col] >= height:
                    break

            for right_col in range(col + 1, n):
                right += 1
                if puzzle[row][right_col] >= height:
                    break

            for up_row in range(row - 1, -1, -1):
                up += 1
                if puzzle[up_row][col] >= height:
                    break

            for down_row in range(row + 1, n):
                down += 1
                if puzzle[down_row][col] >= height:
                    break

            max_score = max(max_score, left * right * up * down)

    return max_score


def part_one(puzzle):
    max_per_coordinate = defaultdict(coordinate)
    n = len(puzzle)

    for row in range(n):
        max_row_left = max_col_up = max_row_right = max_col_down = -1

        for col in range(n):
            max_per_coordinate[(row, col)].left_max = max_row_left
            max_per_coordinate[(row, n - 1 - col)].right_max = max_row_right
            max_per_coordinate[(col, row)].up_max = max_col_up
            max_per_coordinate[(n - 1 - col, row)].down_max = max_col_down

            max_row_left = max(puzzle[row][col], max_row_left)
            max_row_right = max(puzzle[row][n - 1 - col], max_row_right)
            max_col_up = max(puzzle[col][row], max_col_up)
            max_col_down = max(puzzle[n - 1 - col][row], max_col_down)

    return sum(
        any(
            puzzle[row][col] > val
            for val in max_per_coordinate[(row, col)].__dict__.values()
        )
        for row in range(n)
        for col in range(n)
    )


path = "input.txt"
puzzle = get_puzzle(path)
print(f"Part one: {part_one(puzzle)}")
print(f"Part two: {part_two(puzzle)}")
