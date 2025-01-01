def get_input(path):
    with open(path) as file:
        keys, locks = [], []

        for schematic in file.read().split("\n\n"):
            s = schematic.splitlines()
            if s[0][0] == "#":
                counters = [-1] * len(s[0])

                for i in range(len(s[0])):
                    for j in range(len(s)):
                        if s[j][i] == "#":
                            counters[i] += 1

                locks.append(counters)
            else:
                counters = [-1] * len(s[0])

                for i in range(len(s[0])):
                    for j in range(len(s) - 1, -1, -1):
                        if s[j][i] == "#":
                            counters[i] += 1

                keys.append(counters)
        return keys, locks


def part_one(keys, locks):
    return sum(
        all(k + l <= len(key) for k, l in zip(key, lock))
        for key in keys
        for lock in locks
    )


path = "input.txt"
keys, locks = get_input(path)
print(f"Part one: {part_one(keys, locks)}")
