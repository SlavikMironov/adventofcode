instructions = []
directions = {"N": 1j, "S": -1j, "E": 1, "W": -1}
rotate = {
    "L": {
        90: {"N": "W", "S": "E", "E": "N", "W": "S"},
        180: {"N": "S", "S": "N", "E": "W", "W": "E"},
        270: {"N": "E", "S": "W", "E": "S", "W": "N"},
    },
    "R": {
        90: {"N": "E", "S": "W", "E": "S", "W": "N"},
        180: {"N": "S", "S": "N", "E": "W", "W": "E"},
        270: {"N": "W", "S": "E", "E": "N", "W": "S"},
    },
}


def rotate_vector(direction, z: complex, degrees: int):
    if direction == "L":
        if degrees == 90:
            return -z.imag + (z.real) * 1j
        if degrees == 180:
            return -z.real + (-z.imag) * 1j
        return z.imag + (-z.real) * 1j
    if degrees == 90:
        return z.imag + (-z.real) * 1j
    if degrees == 180:
        return -z.real + (-z.imag) * 1j
    return -z.imag + (z.real) * 1j


for line in open("input.txt").read().splitlines():
    direction, steps = line[0], line[1:]
    instructions.append((direction, int(steps)))

d = p = "E"
curr = 0 + 0j


for instruction, steps in instructions:
    if instruction in rotate:
        p = rotate[instruction][steps][p]
        continue
    elif instruction in directions:
        d = instruction

    curr += steps * directions[d if instruction != "F" else p]
print(f"Part one: {int(abs(curr.real) + abs(curr.imag))}")


ship = 0 + 0j
waypoint = 10 + 1j

for instruction, steps in instructions:
    if instruction in "RL":
        waypoint = rotate_vector(instruction, waypoint, steps)
        continue
    elif instruction in directions:
        waypoint += steps * directions[instruction]
    elif instruction == "F":
        ship += steps * waypoint
print(f"Part two: {int(abs(ship.real) + abs(ship.imag))}")
