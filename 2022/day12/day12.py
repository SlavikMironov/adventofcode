from collections import deque


def get_puzzle(path):
    with open(path) as file:
        return list(map(list, file.read().splitlines()))


def get_starting_end_position(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == "S":
                sr, sc = row, col
            elif puzzle[row][col] == "E":
                er, ec = row, col

    return (sr, sc), (er, ec)


def in_range(puzzle, row, col):
    return 0 <= row < len(puzzle) and 0 <= col < len(puzzle[0])


def part_one(puzzle, s_position, e_position):
    (sr, sc), (er, ec) = s_position, e_position
    visited = set()
    puzzle[sr][sc] = "a"
    puzzle[er][ec] = "z"
    q = deque()
    q.append(((sr, sc), 0))
    visited.add((sr, sc))

    while q:
        (row, col), steps = q.popleft()

        if (row, col) == (er, ec):
            puzzle[sr][sc] = "S"
            puzzle[er][ec] = "E"
            return steps

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc
            if (
                in_range(puzzle, nr, nc)
                and (nr, nc) not in visited
                and ord(puzzle[nr][nc]) - ord(puzzle[row][col]) <= 1
            ):
                q.append(((nr, nc), steps + 1))
                visited.add((nr, nc))


def part_two(puzzle, s_position, e_position):
    (sr, sc), (er, ec) = s_position, e_position
    visited = set()
    puzzle[sr][sc] = "a"
    puzzle[er][ec] = "z"
    q = deque()
    q.append(((er, ec), 0))
    visited.add((er, ec))
    m = float("inf")

    while q:
        (row, col), steps = q.popleft()

        if puzzle[row][col] == "a":
            m = min(m, steps)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc
            if (
                in_range(puzzle, nr, nc)
                and (nr, nc) not in visited
                and ord(puzzle[row][col]) - ord(puzzle[nr][nc]) <= 1
            ):
                q.append(((nr, nc), steps + 1))
                visited.add((nr, nc))

    return m


path = "input.txt"
puzzle = get_puzzle(path)
s_position, e_position = get_starting_end_position(puzzle)
print(f"Part one: {part_one(puzzle, s_position, e_position)}")
print(f"Part two: {part_two(puzzle, s_position, e_position)}")
