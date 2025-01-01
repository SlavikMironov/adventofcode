def get_matrix(path):
    with open(path) as file:
        return file.read().split()


def part_two(garden):
    visited = set()
    result = 0

    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) not in visited:
                area, sides, seen = travel_part_two(garden, (i, j))
                visited |= seen
                result += area * sides

    return result


def part_one(garden):
    visited = set()
    result = 0

    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) not in visited:
                area, sides, seen = travel(garden, (i, j))
                visited |= seen
                result += area * sides

    return result


def travel(garden, coordinate):
    row, col = coordinate
    visited = set()
    perimeters = 0

    def dfs(row, col):
        nonlocal perimeters
        if (row, col) in visited:
            return
        visited.add((row, col))

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc
            if is_valid(garden, (row, col), (nr, nc), len(garden), len(garden[0])):
                dfs(nr, nc)
            else:
                perimeters += 1

    dfs(row, col)

    return (
        len(visited),
        perimeters,
        visited,
    )


def travel_part_two(garden, coordinate):
    row, col = coordinate
    visited = set()
    sides = 0

    def dfs(row, col):
        if (row, col) in visited:
            return
        visited.add((row, col))

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc
            if is_valid(garden, (row, col), (nr, nc), len(garden), len(garden[0])):
                dfs(nr, nc)

    dfs(row, col)

    for i, j in visited:
        for first_neighbor, second_neighbor in [
            ((-1, 0), (0, 1)),
            ((1, 0), (0, -1)),
            ((-1, 0), (0, -1)),
            ((1, 0), (0, 1)),
        ]:
            fr, fc = first_neighbor
            sr, sc = second_neighbor
            fr, fc, sr, sc = i + fr, j + fc, i + sr, j + sc
            if not is_valid(
                garden, (row, col), (fr, fc), len(garden), len(garden[0])
            ) and not is_valid(
                garden, (row, col), (sr, sc), len(garden), len(garden[0])
            ):
                sides += 1
            elif is_valid(
                garden,
                (row, col),
                (fr, fc),
                len(garden),
                len(garden[0]),
            ) and is_valid(garden, (row, col), (sr, sc), len(garden), len(garden[0])):
                fr, fc = first_neighbor
                sr, sc = second_neighbor
                diag_r, diag_c = i + fr, j + sc
                if not is_valid(
                    garden, (row, col), (diag_r, diag_c), len(garden), len(garden[0])
                ):
                    sides += 1

    return (
        len(visited),
        sides,
        visited,
    )


def is_valid(garden, curr_coor, next_coor, row_len, col_len):
    return (
        0 <= next_coor[0] < row_len
        and 0 <= next_coor[1] < col_len
        and garden[next_coor[0]][next_coor[1]] == garden[curr_coor[0]][curr_coor[1]]
    )


path = "input.txt"

matrix = get_matrix(path)
print(f"Part one {part_one(matrix)}")
print(f"Part two {part_two(matrix)}")
# input example
# AAAA
# BBCD
# BBCC
# EEEC
