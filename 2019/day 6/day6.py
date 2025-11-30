from collections import defaultdict, deque
from functools import cache

orbits = [tuple(line.split(")")) for line in open("input.txt").read().splitlines()]
graph = defaultdict(list)
graph_part2 = defaultdict(list)

for u, v in orbits:
    graph[v].append(u)
    graph_part2[v].append(u)
    graph_part2[u].append(v)


@cache
def get_total_orbits(node):
    return sum(1 + get_total_orbits(v) for v in graph.get(node, []))


print("Part 1:", sum(get_total_orbits(v) for v in graph))

source, target = "YOU", "SAN"
queue, seen = deque(), set()
targets = set(graph_part2[target])

for v in graph_part2[source]:
    queue.append((v, 0))
    seen.add(v)

while queue:
    node, cost = queue.popleft()

    if node in targets:
        print("Part 2:", cost)
        break

    for v in graph_part2.get(node, []):
        if v not in seen:
            seen.add(v)
            queue.append((v, cost + 1))
