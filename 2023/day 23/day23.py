from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10**6)


maze = open("input.txt").read().splitlines()
n, m = len(maze), len(maze[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
forced_directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
seen = set()


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < m and maze[r][c] != "#"


def get_longest_path(r, c):
    if r == n - 1:
        return 0
    seen.add((r, c))
    max_path = float("-inf")
    if maze[r][c] in forced_directions:
        dr, dc = forced_directions[maze[r][c]]
        nr, nc = r + dr, c + dc

        if is_valid(nr, nc) and (nr, nc) not in seen:
            max_path = 1 + get_longest_path(nr, nc)
    else:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and (nr, nc) not in seen:
                max_path = max(max_path, 1 + get_longest_path(nr, nc))

    seen.remove((r, c))

    return max_path


print(get_longest_path(0, 1))


def build_graph():
    start = (0, 1)
    end = (n - 1, maze[n - 1].index("."))
    junctions = set([start, end])
    graph = defaultdict(list)

    for r in range(n):
        for c in range(m):
            if maze[r][c] != "#":
                neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc):
                        neighbors += 1
                if neighbors > 2:
                    junctions.add((r, c))

    for i, j in junctions:
        q = deque([(i, j, 0)])
        seen = {(i, j)}

        while q:
            r, c, dist = q.popleft()

            if (r, c) in junctions and dist != 0:
                graph[(i, j)].append(((r, c), dist))
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc, dist + 1))

    return graph


graph = build_graph()


def get_longest_path_part2(node):
    if node[0] == n - 1:
        return 0
    visited.add(node)
    max_len = float("-inf")
    for nxt, w in graph[node]:
        if nxt not in visited:
            max_len = max(max_len, w + get_longest_path_part2(nxt))
    visited.remove(node)
    return max_len


visited = set()

print(get_longest_path_part2((0, 1)))
