from typing import Counter


groups = open("input.txt").read().split("\n\n")
res_part1 = 0

for group in groups:
    counter = Counter()
    for answers in group.splitlines():
        for answer in answers:
            counter[answer] += 1
    res_part1 += len(counter)

print(f"Part one {res_part1}")
res_part2 = 0

for group in groups:
    counter = Counter()
    answers = group.splitlines()
    for answer in answers:
        for ans in answer:
            counter[ans] += 1
    for ans in counter:
        if counter[ans] == len(answers):
            res_part2 += 1

print(f"Part two: {res_part2}")
