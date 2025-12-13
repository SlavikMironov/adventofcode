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
        return 1 if prev == target else 0
    if joltages[i] - prev <= 3:
        return number_of_ways(i + 1, joltages[i]) + number_of_ways(i + 1, prev)
    return 0


print(f"Part two: {number_of_ways(0, 0)}")
