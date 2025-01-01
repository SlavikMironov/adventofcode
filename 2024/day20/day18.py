from queue import Queue


def get_input(path):
    with open(path) as file:
        return list(map(list, file.read().splitlines()))


def part_two(maze):
    def get_start_end_coordinates():
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col] == "S":
                    sr, sc = row, col
                elif maze[row][col] == "E":
                    er, ec = row, col

        return (sr, sc), (er, ec)

    (sr, sc), (er, ec) = get_start_end_coordinates()

    def is_valid(row, col, visited):
        return (
            0 <= row < len(maze)
            and 0 <= col < len(maze[0])
            and (row, col) not in visited
            and maze[row][col] != "#"
        )

    def is_valid2(row, col, visited):
        return (
            0 <= row < len(maze)
            and 0 <= col < len(maze[0])
            and (row, col) not in visited
        )

    def bfs(row, col, d, seen):
        q = Queue()
        visited = set()
        visited.add((row, col))
        q.put((row, col, 0))
        cheats = 0

        while not q.empty():
            i, j, distance = q.get()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = i + dr, j + dc

                if is_valid2(nr, nc, visited) and distance + 1 <= 20:
                    if (
                        maze[nr][nc] != "#"
                        and ((row, col), (nr, nc)) not in seen
                        and ((nr, nc), (row, col)) not in seen
                        and abs(d[row, col] - d[nr, nc]) - (distance + 1) >= 100
                    ):
                        seen.add(((row, col), (nr, nc)))
                        seen.add(((nr, nc), (row, col)))
                        cheats += 1
                    visited.add((nr, nc))
                    q.put((nr, nc, distance + 1))

        return cheats

    parent = {}
    d = {}
    q = Queue()
    d[sr, sc] = 0
    parent[sr, sc] = None
    q.put((sr, sc, 0))
    visited = set()
    visited.add((sr, sc))

    while not q.empty():
        row, col, distance = q.get()
        if (row, col) == (er, ec):
            break

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc

            if is_valid(nr, nc, visited):
                d[nr, nc] = distance + 1
                parent[nr, nc] = (row, col)
                visited.add((nr, nc))
                q.put((nr, nc, distance + 1))
    seen = set()
    count = 0
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] != "#":
                count += bfs(row, col, d, seen)

    return count


def part_one(maze):
    def get_start_end_coordinates():
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col] == "S":
                    sr, sc = row, col
                elif maze[row][col] == "E":
                    er, ec = row, col

        return (sr, sc), (er, ec)

    (sr, sc), (er, ec) = get_start_end_coordinates()

    def is_valid(row, col):
        return (
            0 <= row < len(maze)
            and 0 <= col < len(maze[0])
            and maze[row][col] not in "O#"
        )

    parent = {}
    d = {}
    q = Queue()
    d[sr, sc] = 0
    parent[sr, sc] = None
    q.put((sr, sc, 0))
    maze[sr][sc] = "O"
    cheats = 0

    while not q.empty():
        row, col, distance = q.get()
        if (row, col) == (er, ec):
            break

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc

            if is_valid(nr, nc):
                d[nr, nc] = distance + 1
                parent[nr, nc] = (row, col)
                maze[nr][nc] = "O"
                q.put((nr, nc, distance + 1))

    for row in range(1, len(maze) - 1):
        for col in range(1, len(maze[0]) - 1):
            if maze[row][col] == "#":
                for dr, dc in [(1, 0), (0, 1)]:
                    nr1, nc1 = row + dr, col + dc
                    nr2, nc2 = row - dr, col - dc

                    if maze[nr1][nc1] != "#" and maze[nr2][nc2] != "#":
                        if abs(d[nr1, nc1] - d[nr2, nc2]) - 2 >= 100:
                            cheats += 1

    return cheats


path = "input.txt"
maze = get_input(path)

print(f"Part one {part_one(maze)}")
maze = get_input(path)
print(f"Part two: {part_two(maze)}")
