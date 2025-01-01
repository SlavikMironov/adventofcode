from collections import defaultdict


def get_input(path):
    network_map = {}

    with open(path) as file:
        instructions, nodes = file.read().split("\n\n")
        instructions = [0 if instruction == "L" else 1 for instruction in instructions]

        for node in nodes.splitlines():
            key_node, directions = node.split(" = ")
            left_node, right_node = directions.split(", ")
            network_map[key_node] = (left_node[1:], right_node[:-1])

        return network_map, instructions


def part_two(network_map, instructions):
    ghost_network_map = defaultdict(dict)
    steps = 0
    instruction_index = 0
    n = len(instructions)

    for node, nodes in network_map.items():
        ghost_network_map[node[-1]][node] = nodes

    nodes_position = ghost_network_map["A"].keys()
    finished = False

    while True:
        current_nodes_position = []

        if finished:
            break
        finished = True
        for node in nodes_position:
            new_node_position = ghost_network_map[node[-1]][node][
                instructions[instruction_index]
            ]
            current_nodes_position.append(new_node_position)
            if new_node_position[-1] != "Z":
                finished = False
        nodes_position = current_nodes_position
        instruction_index = (instruction_index + 1) % n
        steps += 1

    return steps


def part_one(network_map, instructions):
    current_position, instruction_index, steps, n = "AAA", 0, 0, len(instructions)

    while True:
        if current_position == "ZZZ":
            break
        steps += 1
        current_position = network_map[current_position][
            instructions[instruction_index]
        ]
        instruction_index = (instruction_index + 1) % n

    return steps


path = "input.txt"
network_map, instructions = get_input(path)
# print(f"Part one: {part_one(network_map, instructions)}")
print(f"Part two: {part_two(network_map, instructions)}")
