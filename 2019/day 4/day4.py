from functools import cache
from typing import Counter


l, r = 178416, 676461
digits_len = 6


def get_total_numbers(i, num, adjacent):
    if i == digits_len:
        if adjacent and l <= num <= r:
            return 1
        return 0

    res = 0

    for digit in range(10):
        if i == 0 and digit == 0:
            continue
        if num % 10 <= digit:
            res += get_total_numbers(
                i + 1, num * 10 + digit, True if num % 10 == digit else adjacent
            )

    return res


print(get_total_numbers(0, 0, False))


def get_total_numbers_part2(i, num):
    if i == digits_len:
        if l <= num <= r and any(v == 2 for v in digits_counter.values()):
            return 1
        return 0

    res = 0

    for digit in range(10):
        if i == 0 and digit == 0:
            continue

        if num % 10 <= digit:
            digits_counter[digit] += 1
            res += get_total_numbers_part2(i + 1, num * 10 + digit)
            digits_counter[digit] -= 1

    return res


digits_counter = Counter()

print(get_total_numbers_part2(0, 0))
