def get_maze(path):
    with open(path) as file:
        return file.read().splitlines()


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
CHANGE_DIRECTION = {
    "L": 2,
    "J": 3,
    "7": 2,
    "F": 1,
}


def get_starting_position(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "S":
                return row, col


def part_one(maze):
    sr, sc = get_starting_position(maze)
    dir = 0
    cr, cc = sr + 1, sc
    steps = 1

    while (cr, cc) != (sr, sc):
        if maze[cr][cc] in CHANGE_DIRECTION:
            dir = (dir + CHANGE_DIRECTION[maze[cr][cc]]) % 4
        dr, dc = DIRECTIONS[dir]
        cr, cc = cr + dr, cc + dc
        steps += 1

    return steps // 2


def part_two(maze):
    sr, sc = get_starting_position(maze)
    dir = 0
    cr, cc = sr + 1, sc
    visited = set()
    visited.add((cr, cc))
    count = 0

    while (cr, cc) != (sr, sc):
        if maze[cr][cc] in CHANGE_DIRECTION:
            dir = (dir + CHANGE_DIRECTION[maze[cr][cc]]) % 4
        dr, dc = DIRECTIONS[dir]
        cr, cc = cr + dr, cc + dc
        visited.add((cr, cc))

    # maze[sr][sc] = "7"
    # S in my input is equal to 7
    # S in Jordan input is |, so no need to replace maze[sr][sc] to |
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) not in visited:
                intersections = 0
                k = 0
                cr, cc = row + k, col + k
                while cr < len(maze) and cc < len(maze[0]):
                    cr, cc = row + k, col + k
                    if (cr, cc) in visited and maze[cr][cc] not in "L7":
                        intersections += 1
                    k += 1
                if intersections % 2 == 1:
                    count += 1

    return count


path = "input.txt"

maze = get_maze(path)
print(f"Part one: {part_one(maze)}")
print(f"Part two: {part_two(maze)}")
