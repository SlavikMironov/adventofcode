def get_directions(path):
    with open(path) as file:
        directions = []

        for line in file.read().splitlines():
            direction, steps, rgb = line.split()
            directions.append((direction, int(steps), rgb))

        return directions


def part_two(directions):
    new_directions_map = ["R", "D", "L", "U"]

    return part_one(
        (new_directions_map[int(rgb[-2:-1], 16)], int(rgb[2:-2], 16), "")
        for _, _, rgb in directions
    )


def part_one(directions):
    directions_map = {"U": -1j, "D": 1j, "R": 1, "L": -1}
    cubics = current_vector = area = prev = 0

    for direction, steps, _ in directions:
        current_vector += directions_map[direction] * steps
        cubics += steps
        area += prev.real * current_vector.imag - prev.imag * current_vector.real
        prev = current_vector
    area /= 2

    return int(area + cubics / 2 + 1)


path = "input.txt"

directions = get_directions(path)
print(f"Part one: {part_one(directions)}")
print(f"Part two: {part_two(directions)}")
