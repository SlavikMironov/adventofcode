from collections import Counter, defaultdict
from math import atan2, gcd, pi


grid = open("input.txt").read().splitlines()
n, m = len(grid), len(grid[0])

lines = defaultdict(list)
seen = Counter()

for i in range(n):
    for j in range(m):
        if grid[i][j] == "#":
            x1, y1 = j, i
            for r in range(n):
                for c in range(m):
                    if r == i and c > j or r > i:
                        if grid[r][c] == "#":
                            x2, y2 = c, r
                            if x1 == x2:
                                key = (float("inf"), float("inf"), x1, 1)
                            else:
                                a, b = y2 - y1, x2 - x1
                                c = gcd(abs(a), abs(b))
                                a1, b1 = y1 * x2 - y2 * x1, x2 - x1
                                c1 = gcd(abs(a1), abs(b1))
                                key = (
                                    (-1 if a * b < 0 else 1) * abs(a) // c,
                                    abs(b) // c,
                                    (-1 if a1 * b1 < 0 else 1) * abs(a1) // c1,
                                    abs(b1) // c1,
                                )
                            if (x1, y1) not in lines[key]:
                                lines[key].append((x1, y1))
                            if (x2, y2) not in lines[key]:
                                lines[key].append((x2, y2))

for points in lines.values():
    for i in range(len(points)):
        count = 0
        if i - 1 >= 0:
            count += 1
        if i + 1 < len(points):
            count += 1
        seen[points[i]] += count

max_val = 0
station = (0, 0)

for x, y in seen:
    if seen[(x, y)] > max_val:
        max_val = seen[(x, y)]
        station = (x, y)
print(max_val)

angles = defaultdict(list)
station_x, station_y = station

for y in range(n):
    for x in range(m):
        if grid[y][x] == "#" and (x, y) != station:
            dx = x - station_x
            dy = y - station_y
            angle = atan2(dx, -dy)
            if angle < 0:
                angle += 2 * pi
            dist = dx * dx + dy * dy
            angles[angle].append((dist, (x, y)))

for a in angles:
    angles[a].sort()

sorted_angles = sorted(angles.keys())
count = 0

while count < 200:
    for a in sorted_angles:
        if angles[a]:
            dist, (x, y) = angles[a].pop(0)
            count += 1
            if count == 200:
                print(x * 100 + y)
