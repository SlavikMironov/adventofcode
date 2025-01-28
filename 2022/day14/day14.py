def get_puzzle(path):
    rocks = []

    with open(path) as file:
        for line in file.read().splitlines():
            rocks.append(
                [
                    tuple(map(int, coordinate.split(",")))
                    for coordinate in line.split(" -> ")
                ]
            )

    return rocks


def part_two(rocks, max_x, max_y):
    floor_y = max_y + 2
    cave = [["."] * (max_x + 1000) for _ in range(floor_y + 1)]

    for rock in rocks:
        for i in range(len(rock) - 1):
            x1, y1 = rock[i]
            x2, y2 = rock[i + 1]
            if x1 != x2:
                for j in range(min(x1, x2), max(x1, x2) + 1):
                    cave[y1][j] = "#"
            else:
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    cave[j][x1] = "#"

    for x in range(len(cave[0])):
        cave[floor_y][x] = "#"

    count = 0

    while True:
        can_fall = True
        x, y = 500, 0

        while can_fall:
            can_fall = False
            for dy, dx in [(1, 0), (1, -1), (1, 1)]:
                nx, ny = x + dx, y + dy
                if cave[ny][nx] == ".":
                    x, y = nx, ny
                    can_fall = True
                    break

        if (x, y) == (500, 0):
            return count + 1

        cave[y][x] = "o"
        count += 1


def part_one(rocks, max_x, max_y, min_x):
    cave = [["."] * (max_x + 2) for _ in range(max_y + 2)]

    for rock in rocks:
        for i in range(len(rock) - 1):
            x1, y1 = rock[i]
            x2, y2 = rock[i + 1]
            if x1 != x2:
                for j in range(min(x1, x2), max(x1, x2) + 1):
                    cave[y1][j] = "#"
            else:
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    cave[j][x1] = "#"

    count = 0

    while True:
        can_fall = True
        x, y = 500, 0

        while can_fall:
            can_fall = False
            for dy, dx in [(1, 0), (1, -1), (1, 1)]:
                nx, ny = x + dx, y + dy
                if (
                    min_x - 1 <= nx <= max_x + 1
                    and ny <= max_y + 1
                    and cave[ny][nx] == "."
                ):
                    x, y = nx, ny
                    can_fall = True
                    break

        if (x, y) == (500, 0) or y > max_y:
            return count

        cave[y][x] = "o"
        count += 1


path = "input.txt"
rocks = get_puzzle(path)
max_x = max_y = -1
min_x = float("inf")
for rock in rocks:
    for x, y in rock:
        min_x = min(min_x, x)
        max_x = max(x, max_x)
        max_y = max(y, max_y)

print(f"Part one: {part_one(rocks, max_x, max_y, min_x)}")
print(f"Part two: {part_two(rocks, max_x, max_y)}")
