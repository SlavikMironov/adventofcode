from collections import defaultdict
from itertools import combinations


points = [
    tuple(map(int, line.split(","))) for line in open("input.txt").read().splitlines()
]
n = len(points)


def get_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


m = len(points)
circuits = {}
circuits_l = defaultdict(int)
ids = 0

pairs = list(combinations(points, 2))
pairs.sort(key=lambda p: get_distance(p[0], p[1]))
n = len(pairs)

for i in range(1000):
    p1, p2 = pairs[i]

    if p1 in circuits and p2 in circuits:
        if circuits[p1] == circuits[p2]:
            continue
        circuit_id = circuits[p2]
        circuits_l[circuits[p1]] += circuits_l[circuit_id]
        for key in circuits:
            if circuits[key] == circuit_id:
                circuits[key] = circuits[p1]
        del circuits_l[circuit_id]
    elif p1 in circuits:
        circuits[p2] = circuits[p1]
        circuits_l[circuits[p2]] += 1
    elif p2 in circuits:
        circuits[p1] = circuits[p2]
        circuits_l[circuits[p1]] += 1
    else:
        circuits[p1] = ids
        circuits[p2] = ids
        circuits_l[ids] = 2
        ids += 1

p = 1
res = sorted(circuits_l.values(), reverse=True)
for i in range(3):
    p *= res[i]
print(f"Part one: {p}")


circuits = {}
circuits_l = defaultdict(int)
ids = 0

for i in range(n):
    p1, p2 = pairs[i]

    if p1 in circuits and p2 in circuits:
        if circuits[p1] == circuits[p2]:
            continue
        circuit_id = circuits[p2]
        circuits_l[circuits[p1]] += circuits_l[circuit_id]
        for key in circuits:
            if circuits[key] == circuit_id:
                circuits[key] = circuits[p1]
        del circuits_l[circuit_id]
    elif p1 in circuits:
        circuits[p2] = circuits[p1]
        circuits_l[circuits[p2]] += 1
    elif p2 in circuits:
        circuits[p1] = circuits[p2]
        circuits_l[circuits[p1]] += 1
    else:
        circuits[p1] = ids
        circuits[p2] = ids
        circuits_l[ids] = 2
        ids += 1

    if i != 0 and len(circuits_l) == 1:
        print(f"Part two: {p1[0] * p2[0]}")
        break
