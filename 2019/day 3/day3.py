from typing import Counter


instructions = [
    instruction.split(",") for instruction in open("input.txt").read().splitlines()
]
directions = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
seen = set()
m = float("inf")
intersections = Counter()

for i in range(len(instructions)):
    instruction_i = instructions[i]
    x = y = 0

    for instruction in instruction_i:
        d = instruction[0]
        steps = int(instruction[1:])
        dx, dy = directions[d]

        for _ in range(steps):
            x, y = x + dx, y + dy
            if i == 1 and (x, y) in seen:
                intersections[(x, y)] = 0
                m = min(m, abs(x) + abs(y))
            if i == 0:
                seen.add((x, y))
print(m)

candidates = Counter()
min_steps = float("inf")

for i in range(len(instructions)):
    instruction_i = instructions[i]
    x = y = total_steps = 0

    for instruction in instruction_i:
        d = instruction[0]
        steps = int(instruction[1:])
        dx, dy = directions[d]

        for _ in range(steps):
            total_steps += 1
            x, y = x + dx, y + dy
            if (x, y) in intersections:
                intersections[(x, y)] += total_steps
                if i == 1:
                    min_steps = min(min_steps, intersections[(x, y)])

print(min_steps)
