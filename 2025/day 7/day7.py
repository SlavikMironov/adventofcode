from collections import deque
from functools import cache


maze = open("input.txt").read().splitlines()
n, m = len(maze), len(maze[0])
sr = 0
sc = maze[0].index("S")
splits = 0
queue = deque([(sr, sc)])
seen = {sr, sc}


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < m


while queue:
    r, c = queue.popleft()
    nr, nc = r + 1, c

    if is_valid(nr, nc):
        if maze[nr][nc] == ".":
            queue.append((nr, nc))
            seen.add((nr, nc))
        else:
            splits += 1
            for dc in [-1, 1]:
                nr, nc = r, c + dc

                if is_valid(nr, nc) and (nr, nc) not in seen:
                    queue.append((nr, nc))
                    seen.add((nr, nc))

print(f"Part one: {splits}")


@cache
def get_total_routes(r, c):
    if r == n - 1:
        return 1

    total_routes = 0
    nr, nc = r + 1, c

    if is_valid(nr, nc) and maze[nr][nc] == ".":
        return get_total_routes(nr, nc)

    for dc in [-1, 1]:
        nr, nc = r, c + dc
        if is_valid(nr, nc) and maze[nr][nc] == ".":
            total_routes += get_total_routes(nr, nc)

    return total_routes


print(f"Part two: {get_total_routes(sr, sc)}")
