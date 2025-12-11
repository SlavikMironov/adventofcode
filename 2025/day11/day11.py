from collections import defaultdict
from functools import cache

graph = defaultdict(list)
# Confirm that the graph structure is a DAG

for line in open("input.txt").read().splitlines():
    parts = line.split()
    node = parts[0][:-1]

    for u in parts[1:]:
        graph[node].append(u)


@cache
def get_paths(node):
    if node == "out":
        return 1
    return sum(get_paths(u) for u in graph.get(node, []))


print(f"Part one: {get_paths("you")}")


@cache
def get_paths2(node, c):
    if node == "out":
        return 1 if c == 2 else 0
    if node in ["dac", "fft"]:
        c += 1
    return sum(get_paths2(u, c) for u in graph.get(node, []))


print("Part two:", get_paths2("svr", 0))
