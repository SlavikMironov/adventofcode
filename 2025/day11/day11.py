from collections import defaultdict
from functools import cache

graph = defaultdict(list)
# Confirm that the graph structure is a tree

for line in open("input.txt").read().splitlines():
    parts = line.split()
    node = parts[0][:-1]

    for u in parts[1:]:
        graph[node].append(u)


@cache
def get_paths(node):
    if node == "out":
        return 1

    res = 0

    for u in graph.get(node, []):
        res += get_paths(u)

    return res


print(f"Part one: {get_paths("you")}")


@cache
def get_paths2(node, c):
    if node == "out":
        return 1 if c == 2 else 0
    if node in ["dac", "fft"]:
        c += 1

    total = 0
    for nxt in graph[node]:
        total += get_paths2(nxt, c)
    return total


print("Part two:", get_paths2("svr", 0))
