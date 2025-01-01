def get_mirrors(path):
    mirrors = []

    with open(path) as file:
        for mirror in file.read().split("\n\n"):
            mirrors.append(mirror.splitlines())

    return mirrors


def compare(i, j, mirror):
    return j >= len(mirror) or mirror[i] == mirror[j]


def count_reflects(mirror):
    for line in range(len(mirror) - 1):
        if all(compare(i, 2 * line + 1 - i, mirror) for i in range(line + 1)):
            return line + 1

    return 0


def count_reflects_part_two(mirror1, mirror2):
    bad_rows1 = []
    bad_rows2 = []

    for line in range(len(mirror1) - 1):
        bad_row = []
        for i in range(line + 1):
            if not compare(i, 2 * line + 1 - i, mirror1):
                x = mirror1[i]
                y = mirror1[2 * line + 1 - i]
                differences = 0
                different_index = -1

                for k in range(len(x)):
                    if x[k] != y[k]:
                        differences += 1
                        different_index = i
                bad_row.append(
                    (
                        i,
                        2 * line + 1 - i,
                        different_index,
                        line + 1,
                        differences,
                    )
                )

        if len(bad_row) == 1:
            bad_rows1.append(bad_row)
    bad_rows1 = [bad_r for bad_r in bad_rows1 if bad_r[0][-1] == 1]

    for line in range(len(mirror2) - 1):
        bad_row = []
        for i in range(line + 1):
            if not compare(i, 2 * line + 1 - i, mirror2):
                x = mirror2[i]
                y = mirror2[2 * line + 1 - i]
                differences = 0
                different_index = -1

                for k in range(len(x)):
                    if x[k] != y[k]:
                        differences += 1
                        different_index = i
                bad_row.append(
                    (
                        i,
                        2 * line + 1 - i,
                        different_index,
                        line + 1,
                        differences,
                    )
                )

        if len(bad_row) == 1:
            bad_rows2.append(bad_row)
    bad_rows2 = [bad_r for bad_r in bad_rows2 if bad_r[0][-1] == 1]

    return bad_rows1[0][0][-2] if bad_rows1 else 100 * bad_rows2[0][0][-2]


def part_two(mirrors):
    count = 0

    for mirror in mirrors:
        transposed_mirror = list(map("".join, zip(*mirror)))
        count += count_reflects_part_two(transposed_mirror, mirror)

    return count


def part_one(mirrors):
    count = 0

    for mirror in mirrors:
        transposed_mirror = list(map("".join, zip(*mirror)))
        count += count_reflects(transposed_mirror) + 100 * count_reflects(mirror)

    return count


path = "input.txt"
mirrors = get_mirrors(path)

print(f"Part one: {part_one(mirrors)}")
print(f"Part one: {part_two(mirrors)}")
