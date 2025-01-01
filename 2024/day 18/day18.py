from queue import Queue

X = 6
Y = 6


def get_bytes(path):
    coordinates = []

    with open(path) as file:
        for byte in file.read().splitlines():
            x, y = map(int, byte.split(","))
            coordinates.append((x, y))

    return coordinates


def part_two(bytes_coordinates):
    left = 1
    right = len(bytes_coordinates)

    while left < right:
        middle = (left + right) // 2

        x = part_one(bytes_coordinates, middle)
        y = part_one(bytes_coordinates, middle - 1)

        if y and not x:
            return bytes_coordinates[middle - 1]

        elif x and y:
            left = middle + 1
        else:
            right = middle - 1

    return bytes_coordinates[middle]


def part_one(bytes_coordinates, i):
    bytes_coordinates = set(bytes_coordinates[:i])
    end = (X, Y)
    visited = set()
    queue = Queue()
    queue.put((0, 0, 1))

    while not queue.empty():
        x, y, distance = queue.get()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x, next_y = x + dx, y + dy

            if (next_x, next_y) == end:
                return distance
            if (
                0 <= next_x <= X
                and 0 <= next_y <= Y
                and (next_x, next_y) not in bytes_coordinates
                and (next_x, next_y) not in visited
            ):
                visited.add((next_x, next_y))
                queue.put((next_x, next_y, 1 + distance))


path = "input.txt"
bytes_coordinates = get_bytes(path)


print(f"Part one: {part_one(bytes_coordinates, 1024)}")
print(f"Part two: {part_two(bytes_coordinates)}")
