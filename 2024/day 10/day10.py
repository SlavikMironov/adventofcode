def get_input(path):
    with open(path) as file:
        return [list(map(int, line.strip())) for line in file]


def part_one(matrix):
    return sum(
        travel(matrix, (row, col))
        for row in range(len(matrix))
        for col in range(len(matrix[0]))
        if matrix[row][col] == 0
    )


def travel(matrix, coordinate):
    row, col = coordinate
    count = 0
    visited = set()

    def dfs(row, col):
        nonlocal count

        # if (row, col) in visited:
        #     return
        # visited.add((row, col))

        if matrix[row][col] == 9:
            count += 1

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc
            if (
                in_greed(nr, nc, len(matrix), len(matrix[0]))
                and matrix[nr][nc] == matrix[row][col] + 1
            ):
                dfs(nr, nc)

    dfs(row, col)

    return count


def in_greed(row, col, row_len, col_len):
    return 0 <= row < row_len and 0 <= col < col_len


path = "input.txt"


matrix = get_input(path)

print(f"Part one: {part_one(matrix)}")
