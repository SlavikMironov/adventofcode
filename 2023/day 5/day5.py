import bisect


def get_map(path):
    with open(path) as file:
        maps = []
        args = file.read().split("\n\n")
        seeds = list(map(int, args[0][6:].split()))

        for x_to_y in args[1:]:
            maps.append(parse_map(x_to_y))

        return seeds, maps


def parse_map(map_str: str) -> list[tuple[int]]:
    parsed_list = []

    for x_to_y in map_str.split("\n")[1:]:
        destination, source, range_of_map = x_to_y.split()
        source = int(source)
        destination = int(destination)
        range_of_map = int(range_of_map)
        parsed_list.append((source, source + range_of_map - 1, destination - source))

    parsed_list.sort(key=lambda seed: seed[0])

    return parsed_list


def part_one(seeds, maps):
    locations = []

    for seed in seeds:
        for map in maps:
            for list_map in map:
                start, end, delta = list_map
                if start <= seed <= end:
                    seed += delta
                    break
        locations.append(seed)

    return min(locations)


def binary_search_transform(value, ranges):
    keys = [r[0] for r in ranges]
    index = bisect.bisect_right(keys, value) - 1
    if index >= 0:
        start, end, delta = ranges[index]
        if start <= value <= end:
            return value + delta
    return value


def part_two(seeds, maps):
    locations = []
    new_seeds = []

    for i in range(0, len(seeds), 2):
        new_seeds.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

    for seed in new_seeds:
        seed_ranges = [seed]

        for map in maps:
            additional_seeds = seed_ranges[:]
            seed_ranges_tmp = []

            while additional_seeds:
                s = additional_seeds.pop()

                matched = False
                for start, end, delta in map:

                    if s[1] >= start and s[0] <= end:
                        matched = True

                        overlap_start = max(s[0], start)
                        overlap_end = min(s[1], end)
                        seed_ranges_tmp.append(
                            (overlap_start + delta, overlap_end + delta)
                        )

                        if s[0] < overlap_start:
                            additional_seeds.append((s[0], overlap_start - 1))
                        if s[1] > overlap_end:
                            additional_seeds.append((overlap_end + 1, s[1]))
                        break

                if not matched:
                    seed_ranges_tmp.append(s)
            seed_ranges = seed_ranges_tmp

        locations.extend(seed_ranges)

    return min(location[0] for location in locations)


path = "input.txt"
seeds, maps = get_map(path)


print(f"Part one: {part_one(seeds, maps)}")
print(f"Part two: {part_two(seeds, maps)}")
