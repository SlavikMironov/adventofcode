from collections import deque, defaultdict


def get_maze(path):
    with open(path) as file:
        return file.read().splitlines()


def get_s(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "S":
                return row, col


def part_two(maze):
    sr, sc = get_s(maze)
    visited = set((sr, sc))
    queue = deque([((sr, sc), 0)])
    points = defaultdict(int)
    steps = 26501365

    while queue:
        (row, col), distance_from_s = queue.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc
            if (
                maze[nr % len(maze)][nc % len(maze[0])] != "#"
                and (nr, nc) not in visited
                and distance_from_s + 1 <= 3 * len(maze)
            ):
                visited.add((nr, nc))
                queue.append(((nr, nc), distance_from_s + 1))
                points[distance_from_s + 1] += 1
    x1 = len(maze) // 2
    y1 = sum(val for key, val in points.items() if key <= x1 and key % 2 == x1 % 2)
    x2 = x1 + len(maze)
    y2 = sum(val for key, val in points.items() if key <= x2 and key % 2 == x2 % 2)
    x3 = x2 + len(maze)
    y3 = sum(val for key, val in points.items() if key <= x3 and key % 2 == x3 % 2)
    a = (
        y1 / (x1 * x1 - x1 * x2 - x1 * x3 + x2 * x3)
        + y2 / (-x1 * x2 + x1 * x3 + x2 * x2 - x2 * x3)
        + y3 / (x1 * x2 - x1 * x3 - x2 * x3 + x3 * x3)
    )
    b = (
        -(x2 * y1) / (x1 * x1 - x1 * x2 - x1 * x3 + x2 * x3)
        - (x3 * y1) / (x1 * x1 - x1 * x2 - x1 * x3 + x2 * x3)
        - (x1 * y2) / (-x1 * x2 + x1 * x3 + x2 * x2 - x2 * x3)
        - (x3 * y2) / (-x1 * x2 + x1 * x3 + x2 * x2 - x2 * x3)
        - (x1 * y3) / (x1 * x2 - x1 * x3 - x2 * x3 + x3 * x3)
        - (x2 * y3) / (x1 * x2 - x1 * x3 - x2 * x3 + x3 * x3)
    )
    c = (
        (x2 * x3 * y1) / (x1 * x1 - x1 * x2 - x1 * x3 + x2 * x3)
        + (x1 * x3 * y2) / (-x1 * x2 + x1 * x3 + x2 * x2 - x2 * x3)
        + (x1 * x2 * y3) / (x1 * x2 - x1 * x3 - x2 * x3 + x3 * x3)
    )
    d_from_s = lambda x: round(a * x**2 + b * x + c)
    return d_from_s(steps)


def part_one(maze):
    sr, sc = get_s(maze)
    visited = set((sr, sc))
    queue = deque([((sr, sc), 0)])
    points = defaultdict(int)

    while queue:
        (row, col), distance_from_s = queue.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc
            if (
                0 <= nr < len(maze)
                and 0 <= nc < len(maze[0])
                and maze[nr][nc] != "#"
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                queue.append(((nr, nc), distance_from_s + 1))
                points[distance_from_s + 1] += 1

    return sum(val for key, val in points.items() if key <= 64 and key % 2 == 0)


path = "input.txt"

maze = get_maze(path)
print(f"Part one: {part_one(maze)}")
print(f"Part two: {part_two(maze)}")
