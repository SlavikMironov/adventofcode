import sys

sys.setrecursionlimit(10**6)


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def get_maze(path):
    with open(path) as file:
        return file.read().splitlines()


def part_two(maze):
    m = 0
    for i in [0, len(maze) - 1]:
        for j in range(len(maze[0])):
            if maze[i][j] == ".":
                m = max(m, part_one(maze, i, j, 2 if i == 0 else 3))
    for j in [0, len(maze[0]) - 1]:
        for i in range(len(maze)):
            if maze[i][j] == ".":
                m = max(m, part_one(maze, i, j, 0 if j == 0 else 1))
    return m


def part_one(maze, sr=0, sc=0, curr_dir=0):
    visited = set()
    seen = set()

    def is_valid(row, col):
        return 0 <= row < len(maze) and 0 <= col < len(maze[0])

    def dfs(row, col, direction):
        if (row, col, direction) in visited or not is_valid(row, col):
            return
        visited.add((row, col, direction))
        seen.add((row, col))

        if maze[row][col] in "-":
            if direction in [2, 3]:
                dfs(row, col + 1, 0)
                dfs(row, col - 1, 1)
                return
        if maze[row][col] in "|":
            if direction in [0, 1]:
                dfs(row + 1, col, 2)
                dfs(row - 1, col, 3)
                return

        if maze[row][col] == "/":
            direction = 3 - direction
        elif maze[row][col] == "\\":
            direction = (direction + 2) % 4

        dr, dc = DIRECTIONS[direction]
        dfs(row + dr, col + dc, direction)

    dfs(sr, sc, curr_dir)

    return len(seen)


path = "input.txt"

maze = get_maze(path)


print(f"Part one: {part_one(maze)}")
print(f"Part two: {part_two(maze)}")
