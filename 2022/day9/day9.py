DIRECTION_MAP = {"R": 1j, "L": -1j, "D": -1, "U": 1}


def get_puzzle(path):
    directions = []

    with open(path) as file:
        for line in file.read().splitlines():
            direction, steps = line.split()
            directions.append((DIRECTION_MAP[direction], int(steps)))

    return directions


def part_one(directions):
    visited = set([0])
    head_position = tail_position = 0

    for direction, steps in directions:
        for _ in range(steps):
            head_position += direction

            if abs(head_position - tail_position) > 2**0.5:
                delta = head_position - tail_position
                move = complex(
                    0 if delta.real == 0 else delta.real / abs(delta.real),
                    0 if delta.imag == 0 else delta.imag / abs(delta.imag),
                )
                tail_position += move
                visited.add(tail_position)

    return len(visited)


def part_two(directions):
    visited = set([0])
    head_position = 0
    tails = [0] * 9

    for direction, steps in directions:
        for _ in range(steps):
            head_position += direction

            if abs(head_position - tails[-1]) > 2**0.5:
                delta = head_position - tails[-1]
                move = complex(
                    0 if delta.real == 0 else delta.real / abs(delta.real),
                    0 if delta.imag == 0 else delta.imag / abs(delta.imag),
                )
                tails[-1] += move
                for i in range(7, -1, -1):
                    if abs(tails[i + 1] - tails[i]) > 2**0.5:
                        delta = tails[i + 1] - tails[i]
                        move = complex(
                            0 if delta.real == 0 else delta.real / abs(delta.real),
                            0 if delta.imag == 0 else delta.imag / abs(delta.imag),
                        )
                        tails[i] += move
                visited.add(tails[0])

    return len(visited)


path = "input.txt"
directions = get_puzzle(path)
print(f"Part one: {part_one(directions)}")
print(f"Part two: {part_two(directions)}")
