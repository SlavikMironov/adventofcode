import re

X_AXIS = 101
Y_AXIS = 103


def get_positions(path):
    robots = []

    with open(path) as file:
        for robot in file.read().split("\n"):
            pattern_position = r"p=(\d+),(\d+)"
            pattern_velocity = r"v=(-?\d+),(-?\d+)"
            p = re.search(pattern_position, robot)
            v = re.search(pattern_velocity, robot)
            robots.append(
                ((int(p.group(1)), int(p.group(2))), (int(v.group(1)), int(v.group(2))))
            )

        return robots


def part_one(robots):
    t = 100
    quadrants = [0, 0, 0, 0]
    middle_x = X_AXIS // 2
    middle_y = Y_AXIS // 2

    for robot in robots:
        position, velocity = robot
        final_position = (
            (position[0] + t * velocity[0]) % X_AXIS,
            (position[1] + t * velocity[1]) % Y_AXIS,
        )

        if final_position[0] < middle_x and final_position[1] < middle_y:
            quadrants[0] += 1
        elif final_position[0] > middle_x and final_position[1] < middle_y:
            quadrants[1] += 1
        elif final_position[0] > middle_x and final_position[1] > middle_y:
            quadrants[2] += 1
        elif final_position[0] < middle_x and final_position[1] > middle_y:
            quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def part_two(robots):
    with open("robots_positions.txt", "w") as file:
        for t in range(1, 10001):
            matrix = [["."] * X_AXIS for _ in range(Y_AXIS)]

            for robot in robots:
                position, velocity = robot
                final_position = (
                    (position[0] + t * velocity[0]) % X_AXIS,
                    (position[1] + t * velocity[1]) % Y_AXIS,
                )
                matrix[final_position[1]][final_position[0]] = "*"

            file.write(f"Time = {t}:\n")

            for row in matrix:
                file.write("".join(row) + "\n\n")


path = "input.txt"
robots = get_positions(path)

print(f"Part one: {part_one(robots)}")
part_two(robots)
