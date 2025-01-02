from heapdict import heapdict

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def get_maze(path):
    with open(path) as file:
        return file.read().splitlines()


def part_two(maze):
    def is_valid(i, j):
        return 0 <= i < len(maze) and 0 <= j < len(maze[0])

    def improve(vertex, alt):
        if alt < distance_from_s.get(vertex, float("inf")):
            distance_from_s[vertex] = alt
            return True
        return False

    (sr, sc), (er, ec) = (0, 0), (len(maze) - 1, len(maze[0]) - 1)
    distance_from_s = {}
    priority_queue = heapdict()
    prev_vertexes = set()
    prev_vertexes.add((sr, sc))

    priority_queue[(sr, sc, 0, 1)] = 0
    priority_queue[(sr, sc, 0, 2)] = 0
    distance_from_s[(sr, sc, 0, 1)] = 0
    distance_from_s[(sr, sc, 0, 2)] = 0

    while priority_queue:
        (row, col, prev_steps, direction), score = priority_queue.popitem()

        if prev_steps < 10:
            dr, dc = DIRECTIONS[direction]
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col):
                state = (new_row, new_col, prev_steps + 1, direction)
                new_score = score + int(maze[new_row][new_col])
                if improve(state, new_score):
                    priority_queue[state] = new_score

        if prev_steps >= 4:
            if direction in [0, 1]:
                r = [2, 3]
            else:
                r = [0, 1]
            for d in r:
                dr, dc = DIRECTIONS[d]
                new_row, new_col = row + dr, col + dc
                if is_valid(new_row, new_col):
                    state = (new_row, new_col, 1, d)
                    new_score = score + int(maze[new_row][new_col])
                    if improve(state, new_score):
                        priority_queue[state] = new_score

    return min(
        distance_from_s.get((er, ec, i, j), float("inf"))
        for i in range(4, 11)
        for j in range(4)
    )


def part_one(maze):
    def is_valid(i, j):
        return 0 <= i < len(maze) and 0 <= j < len(maze[0])

    def improve(vertex, alt):
        if alt < distance_from_s.get(vertex, float("inf")):
            distance_from_s[vertex] = alt
            return True
        return False

    (sr, sc), (er, ec) = (0, 0), (len(maze) - 1, len(maze[0]) - 1)
    distance_from_s = {}
    priority_queue = heapdict()
    prev_vertexes = set()
    prev_vertexes.add((sr, sc))

    priority_queue[(sr, sc, 0, 1)] = 0
    priority_queue[(sr, sc, 0, 2)] = 0
    distance_from_s[(sr, sc, 0, 1)] = 0
    distance_from_s[(sr, sc, 0, 2)] = 0

    while priority_queue:
        (row, col, prev_steps, direction), score = priority_queue.popitem()

        if prev_steps < 3:
            dr, dc = DIRECTIONS[direction]
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col):
                state = (new_row, new_col, prev_steps + 1, direction)
                new_score = score + int(maze[new_row][new_col])
                if improve(state, new_score):
                    priority_queue[state] = new_score

        if direction in [0, 1]:
            r = [2, 3]
        else:
            r = [0, 1]
        for d in r:
            dr, dc = DIRECTIONS[d]
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col):
                state = (new_row, new_col, 1, d)
                new_score = score + int(maze[new_row][new_col])
                if improve(state, new_score):
                    priority_queue[state] = new_score

    return min(
        distance_from_s.get((er, ec, i, j), float("inf"))
        for i in range(4)
        for j in range(4)
    )


path = "input.txt"

maze = get_maze(path)
print(f"Part one: {part_one(maze)}")
print(f"Part one: {part_two(maze)}")
