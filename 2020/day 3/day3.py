maze = open("input.txt").read().splitlines()
n, m = len(maze), len(maze[0])
res_part1 = 0
res_part2 = 1


def get_trees(sr, sc):
    res = 0
    r = c = 0

    while r != n - 1:
        r, c = (r + sr) % n, (c + sc) % m
        if maze[r][c] == "#":
            res += 1
    return res


print(f"Part one: {get_trees(1, 3)}")

for dr, dc in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    res_part2 *= get_trees(dr, dc)

print(f"Part two: {res_part2}")
