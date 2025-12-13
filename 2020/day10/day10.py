from functools import cache
from typing import Counter


joltages = list(map(int, open("input.txt").read().splitlines()))
joltages.sort()
n = len(joltages)
count = Counter(joltages[i] - joltages[i - 1] for i in range(1, n))
count[joltages[0]] += 1
count[3] += 1
target = joltages[-1]


print(f"Part one: {count[1] * count[3]}")


@cache
def number_of_ways(i, prev):
    if i == n:
        if prev == target:
            return 1
        return 0

    res = 0

    if joltages[i] - prev <= 3:
        res += number_of_ways(i + 1, joltages[i])

    return number_of_ways(i + 1, prev) + res


print(f"Part two: {number_of_ways(0, 0)}")
