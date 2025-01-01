from math import ceil


def get_input(path):
    with open(path) as file:
        times, distances = file.read().splitlines()
        times = list(map(int, times.replace("Time:", "").lstrip().split()))
        distances = list(map(int, distances.replace("Distance:", "").lstrip().split()))

        return times, distances


def part_one(times, distances):
    counters = []
    for time, distance in zip(times, distances):
        count = 0
        for t in range(1, time):
            t2 = ceil(distance / t) if distance % t else ceil(distance / t) + 1

            if t + t2 <= time:
                count += 1
        counters.append(count)
    p = 1
    for counter in counters:
        p *= counter
    return p


def part_two(times, distances):
    return part_one(
        [int("".join(map(str, times)))], [int("".join(map(str, distances)))]
    )


path = "input.txt"

times, distances = get_input(path)

print(f"Part one: {part_one(times, distances)}")
print(f"Part two: {part_two(times, distances)}")
# Time:      7  15   30
# Distance:  9  40  200
