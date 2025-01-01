from functools import cache


def get_springs(path):
    with open(path) as file:
        springs_list = []

        for row in file.read().splitlines():
            springs, sizes_of_damaged_springs = row.split()
            sizes_of_damaged_springs = tuple(
                map(int, sizes_of_damaged_springs.split(","))
            )
            springs_list.append((springs, sizes_of_damaged_springs))

    return springs_list


def compare_spring(spring, damaged_springs):
    actual_damages_springs = []
    start_seq = -1
    spring += "."

    for index, s in enumerate(spring):
        if s == "#":
            if start_seq == -1:
                start_seq = index
        else:
            if start_seq != -1:
                actual_damages_springs.append(index - start_seq)
                start_seq = -1

    return actual_damages_springs == damaged_springs


def part_one(springs):
    count = 0

    @cache
    def number_of_arrangements_2(spring, damaged_springs, curr_len=0):
        if not spring:
            if curr_len == 0 and not damaged_springs:
                return 1
            if damaged_springs and damaged_springs[0] == curr_len:
                return 1
            return 0

        result = 0

        if spring[0] in ".?":
            if curr_len == 0:
                result += number_of_arrangements_2(spring[1:], damaged_springs, 0)
            elif damaged_springs and curr_len == damaged_springs[0]:
                result += number_of_arrangements_2(spring[1:], damaged_springs[1:], 0)

        if spring[0] in "#?":
            if damaged_springs:
                if curr_len + 1 < damaged_springs[0]:
                    result += number_of_arrangements_2(
                        spring[1:], damaged_springs, curr_len + 1
                    )
                if curr_len + 1 == damaged_springs[0]:
                    if len(spring) == 1 or spring[1] != "#":
                        result += number_of_arrangements_2(
                            spring[2:], damaged_springs[1:], 0
                        )

        return result

    @cache
    def number_of_arrangements(spring, damaged_springs):
        i = len(spring) - 1
        prev = -1
        k = len(damaged_springs) - 1

        while i >= -1:
            if i == -1 or spring[i] == ".":
                if prev != -1:
                    if k < 0 or damaged_springs[k] != prev - i:
                        return 0
                    k -= 1
                    prev = -1
            elif spring[i] == "#":
                if prev == -1:
                    prev = i
            else:
                break
            i -= 1

        if i < 0:
            return 1 if k == -1 else 0

        good_spring = spring[:i] + "." + spring[i + 1 :]
        damaged_spring = spring[:i] + "#" + spring[i + 1 :]

        return number_of_arrangements(
            good_spring, damaged_springs
        ) + number_of_arrangements(damaged_spring, damaged_springs)

    @cache
    def number_of_arrangements_3(spring, damaged_springs):
        if not damaged_springs:
            return 1 if "#" not in spring else 0
        if not spring:
            return 1 if not damaged_springs else 0

        result = 0
        if spring[0] in ".?":
            result += number_of_arrangements_3(spring[1:], damaged_springs)
        if spring[0] in "#?":
            if (
                damaged_springs[0] <= len(spring)
                and "." not in spring[: damaged_springs[0]]
                and (
                    damaged_springs[0] == len(spring)
                    or spring[damaged_springs[0]] != "#"
                )
            ):
                result += number_of_arrangements_3(
                    spring[damaged_springs[0] + 1 :], damaged_springs[1:]
                )
        return result

    for spring_tup in springs:
        spring, damaged_springs_sizes = spring_tup
        count += number_of_arrangements_3(spring, damaged_springs_sizes)

    return count


def part_two(springs):
    count = 0

    @cache
    def number_of_arrangements_2(spring, damaged_springs, curr_len=0):
        if not spring:
            if curr_len == 0 and not damaged_springs:
                return 1
            if damaged_springs and damaged_springs[0] == curr_len:
                return 1
            return 0

        result = 0

        if spring[0] in ".?":
            if curr_len == 0:
                result += number_of_arrangements_2(spring[1:], damaged_springs, 0)
            elif damaged_springs and curr_len == damaged_springs[0]:
                result += number_of_arrangements_2(spring[1:], damaged_springs[1:], 0)

        if spring[0] in "#?":
            if damaged_springs:
                if curr_len + 1 < damaged_springs[0]:
                    result += number_of_arrangements_2(
                        spring[1:], damaged_springs, curr_len + 1
                    )
                if curr_len + 1 == damaged_springs[0]:
                    if len(spring) == 1 or spring[1] != "#":
                        result += number_of_arrangements_2(
                            spring[2:], damaged_springs[1:], 0
                        )

        return result

    @cache
    def number_of_arrangements(spring, damaged_springs):
        i = len(spring) - 1
        prev = -1
        k = len(damaged_springs) - 1

        while i >= -1:
            if i == -1 or spring[i] == ".":
                if prev != -1:
                    if k < 0 or damaged_springs[k] != prev - i:
                        return 0
                    k -= 1
                    prev = -1
            elif spring[i] == "#":
                if prev == -1:
                    prev = i
            else:
                break
            i -= 1

        if i < 0:
            return 1 if k == -1 else 0

        good_spring = spring[:i] + "." + spring[i + 1 :]
        damaged_spring = spring[:i] + "#" + spring[i + 1 :]
        return number_of_arrangements(
            good_spring, damaged_springs
        ) + number_of_arrangements(damaged_spring, damaged_springs)

    @cache
    def number_of_arrangements_3(spring, damaged_springs):
        if not damaged_springs:
            return 1 if "#" not in spring else 0
        if not spring:
            return 1 if not damaged_springs else 0

        result = 0
        if spring[0] in ".?":
            result += number_of_arrangements_3(spring[1:], damaged_springs)
        if spring[0] in "#?":
            if (
                damaged_springs[0] <= len(spring)
                and "." not in spring[: damaged_springs[0]]
                and (
                    damaged_springs[0] == len(spring)
                    or spring[damaged_springs[0]] != "#"
                )
            ):
                result += number_of_arrangements_3(
                    spring[damaged_springs[0] + 1 :], damaged_springs[1:]
                )
        return result

    for spring_tup in springs:
        spring, damaged_springs_sizes = spring_tup
        count += number_of_arrangements_3(
            "?".join([spring] * 5), damaged_springs_sizes * 5
        )

    return count


path = "input.txt"

springs = get_springs(path)

print(f"Part one: {part_one(springs)}")
print(f"Part two: {part_two(springs)}")
