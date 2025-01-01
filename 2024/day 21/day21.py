from collections import deque

DIRECTIONAL_KEYPAD_GRAPH = {
    "A": [("^", "<"), (">", "v")],
    "^": [("v", "v"), ("A", ">")],
    ">": [("A", "^"), ("v", "<")],
    "v": [("^", "^"), ("<", "<"), (">", ">")],
    "<": [("v", ">")],
}

NUMERIC_KEYPAD_GRAPH = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("4", "^"), ("2", ">")],
    "2": [("5", "^"), ("1", "<"), ("0", "v"), ("3", ">")],
    "3": [("6", "^"), ("2", "<"), ("A", "v")],
    "4": [("7", "^"), ("1", "v"), ("5", ">")],
    "5": [("8", "^"), ("4", "<"), ("2", "v"), ("6", ">")],
    "6": [("9", "^"), ("5", "<"), ("3", "v")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("7", "<"), ("5", "v"), ("9", ">")],
    "9": [("8", "<"), ("6", "v")],
    "A": [("3", "^"), ("0", "<")],
}


def get_codes(path):
    with open(path) as file:
        return file.read().splitlines()


def part_two(codes):
    s = 0
    numeric_shortest_paths = shortest_paths_from_all_to_all(NUMERIC_KEYPAD_GRAPH)
    directional_shortest_paths = shortest_paths_from_all_to_all(
        DIRECTIONAL_KEYPAD_GRAPH
    )

    def shortest_path(keys, depth, memory):
        if depth == 0:
            return len(keys)
        if (keys, depth) in memory:
            return memory[(keys, depth)]

        sub_keys = keys.split("A")[:-1]

        memory[(keys, depth)] = sum(
            min(
                shortest_path(sequence, depth - 1, memory)
                for sequence in shortest_code_paths(
                    [sub_key + "A"], directional_shortest_paths
                )
            )
            for sub_key in sub_keys
        )

        return memory[(keys, depth)]

    for code in codes:

        code_paths = shortest_code_paths([code], numeric_shortest_paths)
        mins = []

        for _code in code_paths:
            memory = {}
            mins.append(shortest_path(_code, 25, memory))

        s += min(mins) * int(code[:-1])

    return s


def part_one(codes):
    s = 0

    numeric_shortest_paths = shortest_paths_from_all_to_all(NUMERIC_KEYPAD_GRAPH)
    directional_shortest_paths = shortest_paths_from_all_to_all(
        DIRECTIONAL_KEYPAD_GRAPH
    )
    for code in codes:
        code_paths = shortest_code_paths([code], numeric_shortest_paths)

        code_paths = shortest_code_paths(
            shortest_code_paths(code_paths, directional_shortest_paths),
            directional_shortest_paths,
        )

        s += len(min(code_paths, key=len)) * int(code[:-1])

    return s


def shortest_paths_from_all_to_all(graph):
    shortest_paths = {}

    for node1 in graph.keys():
        for node2 in graph.keys():
            paths = bfs_shortest_paths(graph, node1, node2)
            shortest_paths[(node1, node2)] = [
                "".join(path)
                for path in paths
                if all(
                    not (path[i] == path[i + 2] and path[i + 1] != path[i])
                    for i in range(len(path) - 3)
                )
            ]

    return shortest_paths


def shortest_code_paths(list_of_codes, shortest_paths_dict):
    codes_paths = []

    for code in list_of_codes:
        prev = "A"
        paths = [""]

        for key in code:
            new_paths = []

            for path in paths:
                for short_path in shortest_paths_dict[prev, key]:
                    new_paths.append(path + short_path)
            paths = new_paths
            prev = key
        codes_paths.extend(paths)

    return codes_paths


def bfs_shortest_paths(graph, source, target):
    queue = deque([source])
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    paths = {node: [] for node in graph}

    while queue:
        current = queue.popleft()

        for neighbor_node, neighbor_direction in graph[current]:
            if distances[neighbor_node] > distances[current] + 1:
                distances[neighbor_node] = distances[current] + 1
                queue.append(neighbor_node)
                if paths[current]:
                    paths[neighbor_node] = [
                        path + [neighbor_direction] for path in paths[current]
                    ]
                else:
                    paths[neighbor_node] = [[neighbor_direction]]

            elif distances[neighbor_node] == distances[current] + 1:
                paths[neighbor_node].extend(
                    [path + [neighbor_direction] for path in paths[current]]
                )
    if paths[target]:
        for path in paths[target]:
            path.append("A")
    else:
        paths[target] = [["A"]]

    return paths[target]


path = "input.txt"
codes = get_codes(path)
print(f"Part one: {part_one(codes)}")
print(f"Part two: {part_two(codes)}")
