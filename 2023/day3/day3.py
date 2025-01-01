from collections import defaultdict


def get_matrix(path: str) -> list[str]:
    with open(path) as file:
        return file.read().split("\n")


def part_two(matrix: list[str]) -> int:
    def is_valid(row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

    s = 0
    symbols_map = defaultdict(list)

    for row in range(len(matrix)):
        last_digit_index = -1
        coordinates = []

        for col in range(len(matrix[0])):
            if not matrix[row][col].isdigit():
                if last_digit_index != -1:
                    coordinates.append((last_digit_index, col - 1))
                    last_digit_index = -1
            else:
                if last_digit_index == -1:
                    last_digit_index = col
        if matrix[row][col].isdigit():
            coordinates.append((last_digit_index, col))

        for coordinate in coordinates:
            start, end = coordinate
            found_symbol = False

            for j in range(start, end + 1):
                if found_symbol:
                    break
                for dr, dc in [
                    (-1, 0),
                    (1, 0),
                    (0, 1),
                    (0, -1),
                    (-1, 1),
                    (1, 1),
                    (1, -1),
                    (-1, -1),
                ]:
                    nr, nc = row + dr, j + dc

                    if is_valid(nr, nc):
                        if matrix[nr][nc] == "*":
                            found_symbol = True
                            symbols_map[(nr, nc)].append((row, coordinate))
                            break

    for coordinates in symbols_map.values():
        m = 1
        if len(coordinates) > 1:
            for coordinate in coordinates:
                m *= int(matrix[coordinate[0]][coordinate[1][0] : coordinate[1][1] + 1])
            s += m
    return s


def part_one(matrix: list[str]) -> int:
    def is_valid(row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

    s = 0

    for row in range(len(matrix)):
        last_digit_index = -1
        coordinates = []

        for col in range(len(matrix[0])):
            if not matrix[row][col].isdigit():
                if last_digit_index != -1:
                    coordinates.append((last_digit_index, col - 1))
                    last_digit_index = -1
            else:
                if last_digit_index == -1:
                    last_digit_index = col
        if matrix[row][col].isdigit():
            coordinates.append((last_digit_index, col))

        for coordinate in coordinates:
            start, end = coordinate
            found_symbol = False

            for j in range(start, end + 1):
                if found_symbol:
                    break
                for dr, dc in [
                    (-1, 0),
                    (1, 0),
                    (0, 1),
                    (0, -1),
                    (-1, 1),
                    (1, 1),
                    (1, -1),
                    (-1, -1),
                ]:
                    nr, nc = row + dr, j + dc

                    if is_valid(nr, nc):
                        if not matrix[nr][nc].isdigit() and matrix[nr][nc] != ".":
                            found_symbol = True
                            break
            if found_symbol:
                s += int(matrix[row][start : end + 1])

    return s


path = "input.txt"
matrix = get_matrix(path)
print(f"Part one: {part_one(matrix)}")
print(f"Part two: {part_two(matrix)}")
