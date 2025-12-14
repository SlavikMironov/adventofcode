from collections import defaultdict


grid = list(map(list, open("input.txt").read().splitlines()))
n, m = len(grid), len(grid[0])
changes = False
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


while True:
    cpy_grid = [grid[i].copy() for i in range(n)]
    changes = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] != ".":
                count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == "#":
                        count += 1
                if grid[i][j] == "L":
                    if count == 0:
                        cpy_grid[i][j] = "#"
                        changes = True
                else:
                    if count >= 4:
                        cpy_grid[i][j] = "L"
                        changes = True
    grid = cpy_grid
    if not changes:
        break

print(f"Part one: {sum(1 for i in range(n) for j in range(m) if grid[i][j] == "#")}")


while True:
    seen = defaultdict(set)
    cpy_grid = [grid[i].copy() for i in range(n)]
    changes = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] != ".":
                count = 0

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    while 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == ".":
                        ni, nj = ni + di, nj + dj

                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == "#":
                            seen[(di, dj)].add((ni, nj))
                            count += 1

                if grid[i][j] == "L":
                    if count == 0:
                        cpy_grid[i][j] = "#"
                        changes = True
                else:
                    if count >= 5:
                        cpy_grid[i][j] = "L"
                        changes = True

    grid = cpy_grid
    if not changes:
        break
print(f"Part two: {sum(1 for i in range(n) for j in range(m) if grid[i][j] == "#")}")
