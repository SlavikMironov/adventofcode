from heapdict import heapdict
from collections import defaultdict


DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def get_maze(path):
    with open(path) as file:
        return file.read().split("\n")


def get_starting_end_location(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "S":
                starting_location = (row, col)
            elif maze[row][col] == "E":
                end_location = (row, col)

    return starting_location, end_location


def part_two(maze):
    def is_valid(row, col):
        return (
            0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#"
        )

    def get_paths(p):
        if not p:
            return

        for vertex in p:
            visited.add((vertex[0], vertex[1]))
            get_paths(prev[vertex])

    def improve(vertex, prev_vertex, alt):
        if alt <= distance_from_s.get(vertex, float("inf")):
            distance_from_s[vertex] = alt
            priority_queue[vertex] = alt
            prev[vertex].append(prev_vertex)

    (sr, sc), (er, ec) = get_starting_end_location(maze)
    distance_from_s = {}
    priority_queue = heapdict()
    prev = defaultdict(list)

    priority_queue[(sr, sc, 2)] = 0
    distance_from_s[(sr, sc, 2)] = 0

    while priority_queue:
        (row, col, direction), score = priority_queue.popitem()
        dr, dc = DIRECTIONS[direction]
        new_row, new_col = row + dr, col + dc

        if is_valid(new_row, new_col):
            improve((new_row, new_col, direction), (row, col, direction), score + 1)

        for new_direction in range(4):
            if new_direction != direction:
                improve((row, col, new_direction), (row, col, direction), score + 1000)

    min_v = min(
        [(er, ec, i) for i in range(4)],
        key=lambda vertex: distance_from_s.get(vertex, float("inf")),
    )

    visited = set()
    get_paths(prev[min_v])

    return len(visited) + 1


def part_one(maze):
    def is_valid(row, col):
        return (
            0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#"
        )

    def improve(vertex, prev_vertex, alt):
        if alt < distance_from_s.get(vertex, float("inf")):
            distance_from_s[vertex] = alt
            priority_queue[vertex] = alt
            prev[vertex] = prev_vertex

    (sr, sc), (er, ec) = get_starting_end_location(maze)
    distance_from_s = {}
    priority_queue = heapdict()
    prev = {}
    prev_vertexes = set()
    prev_vertexes.add((sr, sc))

    priority_queue[(sr, sc, 2)] = 0
    distance_from_s[(sr, sc, 2)] = 0

    while priority_queue:
        (row, col, direction), score = priority_queue.popitem()
        dr, dc = DIRECTIONS[direction]
        new_row, new_col = row + dr, col + dc

        if is_valid(new_row, new_col):
            improve((new_row, new_col, direction), (row, col, direction), score + 1)

        for new_direction in range(4):
            if new_direction != direction:
                improve((row, col, new_direction), (row, col, direction), score + 1000)

    min_v = min(
        [(er, ec, i) for i in range(4)],
        key=lambda vertex: distance_from_s.get(vertex, float("inf")),
    )

    return distance_from_s[min_v]


path = "input.txt"

maze = get_maze(path)
print(f"Part one: {part_one(maze)}")
print(f"Part two: {part_two(maze)}")
