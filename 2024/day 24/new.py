import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
import sys
from itertools import combinations


def get_input(path):
    msb = 0
    variables = {}
    graph = defaultdict(list)
    bool_equations = {}

    with open(path) as file:
        wires, gates = file.read().split("\n\n")

        for wire in wires.splitlines():
            variable, bit = wire.split(":")
            variables[variable] = bool(int(bit))

        for gate in gates.splitlines():
            operation, result = gate.split(" -> ")
            if result.startswith("z"):
                msb = max(msb, int(result[1:]))
            v1, op, v2 = operation.split()
            bool_equations[result] = (v1, op, v2)

            graph[v1].append(result)
            graph[v2].append(result)

    return msb, variables, graph, bool_equations


def topological_sort(graph):
    stack = []
    visited = set()

    def dfs(node):
        visited.add(node)

        for child in graph[node]:
            if child not in visited:
                dfs(child)

        stack.append(node)

    for node in list(graph.keys()):
        if node not in visited:
            dfs(node)

    return stack[::-1]


def part_two(msb, variables, graph, bool_equations):
    gates = {}
    gates_graph = defaultdict(list)

    for eq in bool_equations:
        gates[eq[-1]] = (eq[0], eq[1], eq[2])
        gates_graph[eq[0]].append(eq[-1])
        gates_graph[eq[1]].append(eq[-1])

    topological_order = topological_sort(graph)
    bool_equations.sort(key=lambda eq: topological_order[eq[-1]])

    bits = []
    bits_x, bits_y = [], []

    for v1, op, v2, v3 in bool_equations:
        if op == "AND":
            res = variables[v1] & variables[v2]
        elif op == "XOR":
            res = variables[v1] ^ variables[v2]
        else:
            res = variables[v1] | variables[v2]

        variables[v3] = res

    for i in range(msb, -1, -1):
        bits.append(str(int(variables[f"z{i:02}"])))

    for i in range(msb, -1, -1):
        if f"x{i:02}" in variables:
            bits_x.append(str(int(variables[f"x{i:02}"])))

    for i in range(msb, -1, -1):
        if f"y{i:02}" in variables:
            bits_y.append(str(int(variables[f"y{i:02}"])))
    bad_z = "".join(bits)
    good_z = bin(int("".join(bits_x), 2) + int("".join(bits_y), 2))[2:]
    bad_bits = []
    for i in range(len(bad_z)):
        if bad_z[i] != good_z[i]:
            bad_bits.append(msb - i)

    print(f"x bits: {"".join(bits_x)}")
    print(f"y bits: {"".join(bits_y)}")
    print(f"bad z bits: {"".join(bits)}")
    print(f"good z bits: {bin(int("".join(bits_x), 2) + int("".join(bits_y), 2))[2:]}")
    print(f"bad bits: {bad_bits}")
    return bad_bits


def get_bit(bit, variables, graph, bool_equations):
    topological_order = topological_sort(graph)

    for v in topological_order:
        if v[0] not in "xy":
            v1, op, v2 = bool_equations[v]
            if op == "AND":
                res = variables[v1] & variables[v2]
            elif op == "XOR":
                res = variables[v1] ^ variables[v2]
            else:
                res = variables[v1] | variables[v2]

            variables[v] = res

    return variables[f"z{bit:02}"]


def part_one(msb, variables, graph, bool_equations):
    topological_order = topological_sort(graph)
    bits = []

    for v in topological_order:
        if v[0] not in "xy":
            v1, op, v2 = bool_equations[v]
            if op == "AND":
                res = variables[v1] & variables[v2]
            elif op == "XOR":
                res = variables[v1] ^ variables[v2]
            else:
                res = variables[v1] | variables[v2]

            variables[v] = res

    for i in range(msb, -1, -1):
        bits.append(str(int(variables[f"z{i:02}"])))

    return int("".join(bits), 2)


def draw_regular_graph(graph):
    import matplotlib.pyplot as plt
    import networkx as nx

    G = nx.DiGraph()

    # יצירת הקשתות
    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge)

    # שימוש בפריסה אוטומטית
    pos = nx.spring_layout(G)  # אפשר להחליף ל-kamada_kawai_layout אם תרצה

    # שרטוט הצמתים והקשתות
    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="lightblue", alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_size=12, font_color="black")

    # שרטוט הקשתות
    nx.draw_networkx_edges(
        G, pos, arrowstyle="->", arrowsize=20, edge_color="gray", width=1.5, alpha=0.7
    )

    # הוספת כותרת והצגת הגרף
    plt.title("Regular Graph Visualization", fontsize=16)
    plt.axis("off")
    plt.show()


def get_sub_nodes(v, graph):
    visited = set()

    def dfs(v):
        visited.add(v)

        for u in graph[v]:
            if u not in visited:
                dfs(u)

    dfs(v)

    return list(visited)


def get_sub_graph(nodes, graph):
    nodes_set = set(nodes)
    sub_graph = {}

    for node in nodes:
        sub_graph[node] = nodes_set & set(graph[node])

    return sub_graph


def draw_tree_hierarchy(graph):
    import matplotlib.pyplot as plt
    import networkx as nx

    G = nx.DiGraph()

    # יצירת הקשתות
    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge)

    # חיפוש שורש העץ
    all_nodes = set(G.nodes)
    child_nodes = set(edge[1] for edge in G.edges)
    root_nodes = list(all_nodes - child_nodes)

    if not root_nodes:
        print("Cannot draw tree: No root found.")
        return
    elif len(root_nodes) > 1:
        print(f"Cannot draw tree: Multiple roots found: {root_nodes}")
        return

    root = root_nodes[0]

    # יצירת פריסה היררכית ידנית
    pos = _manual_hierarchy_pos(G, root)

    # שרטוט הצמתים והקשתות
    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="lightblue", alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_size=12, font_color="black")
    nx.draw_networkx_edges(
        G, pos, arrowstyle="->", arrowsize=20, edge_color="gray", width=1.5, alpha=0.7
    )

    # הוספת כותרת והצגת העץ
    plt.title("Tree Visualization - Hierarchy Layout", fontsize=16)
    plt.axis("off")
    plt.show()


def _manual_hierarchy_pos(
    G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None
):
    """פריסה היררכית ידנית לעץ."""
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)

    neighbors = list(G.neighbors(root))
    if parent is not None:  # הוצאת האב מרשימת השכנים
        neighbors = [n for n in neighbors if n != parent]

    if len(neighbors) != 0:
        dx = width / len(neighbors)  # חלוקה לרוחב בין השכנים
        next_x = xcenter - width / 2 - dx / 2
        for neighbor in neighbors:
            next_x += dx
            pos = _manual_hierarchy_pos(
                G,
                neighbor,
                width=dx,
                vert_gap=vert_gap,
                vert_loc=vert_loc - vert_gap,
                xcenter=next_x,
                pos=pos,
                parent=root,
            )
    return pos


def get_eq(v, bool_equations, variables):
    # v = "z05"
    gates = {}
    # memo = {}

    for eq in bool_equations:
        gates[eq[-1]] = (eq[0], eq[1], eq[2])
    for v in variables:
        if v[0] in "xy":
            gates[v] = (v, v, v)

    def helper(eq):
        # if eq in memo:
        #     return memo[eq]
        if eq[0][0] in "xy" and eq[2][0] in "xy":
            return f"({eq[0]})"

        # memo[eq] = helper(gates[eq[0]]) + eq[1] + helper(gates[eq[2]])
        return helper(gates[eq[0]]) + eq[1] + helper(gates[eq[2]])

    eq_str = helper(gates[v])

    return f"{v}={eq_str}"


def swap_gates(bit, eq_gates, variables, gates, graph, exp):
    c = []
    for gate1, gate2 in combinations(gates, 2):
        if gate1 not in "xy" or gate2 not in "xy":
            eq_gates[gate1], eq_gates[gate2] = eq_gates[gate2], eq_gates[gate1]
            s_graph = get_sub_graph(eq_gates, graph)
            b = get_bit(bit, variables, s_graph, eq_gates)
            if b == exp:
                c.append([gate1, gate2])

    return c


path = "input.txt"

msb, variables, graph, bool_equations = get_input(path)
print(part_one(msb, variables, graph, bool_equations))
swap_gates(
    5,
    bool_equations,
    variables,
)
# eq_gates = {}

# for v1, op, v2, result in bool_equations:
#     eq_gates[result] = (v1, op, v2)


# reverse_graph = defaultdict(list)

# for v in graph:
#     for u in graph[v]:
#         reverse_graph[u].append(v)
# sub_nodes = {}
# counters = defaultdict(int)
# bad_gates = set()
# for bad_bit in bad_bits:
#     s = get_sub_nodes(f"z{bad_bit:02}", reverse_graph)
#     sub_nodes[bad_bit] = s
#     for node in s:
#         if node[0] not in "xy":
#             counters[node] += 1
#             bad_gates.add(node)
# sorted_dict = dict(sorted(counters.items(), key=lambda item: item[1]))


# x = get_eq("z06", bool_equations, variables)
# print(x)


# nodes1 = get_sub_nodes("z05", reverse_graph)
# nodes2 = get_sub_nodes("z06", reverse_graph)
# nodes3 = get_sub_nodes("z07", reverse_graph)
# nodes4 = get_sub_nodes("z08", reverse_graph)
# nodes5 = get_sub_nodes("z09", reverse_graph)
# nodes6 = get_sub_nodes("z10", reverse_graph)
# nodes7 = get_sub_nodes("z11", reverse_graph)
# nodes8 = get_sub_nodes("z15", reverse_graph)
# nodes9 = get_sub_nodes("z30", reverse_graph)
# nodes10 = get_sub_nodes("z31", reverse_graph)
# n1 = set(nodes1) & set(nodes2) & set(nodes3) & set(nodes4)
# n2 = set(nodes6) & set(nodes7) & set(nodes8) & set(nodes9) & set(nodes10)
# print(n2)
# sub_g = get_sub_graph(bad_gates, reverse_graph)

# print(f"Part one: {part_one(msb, variables, graph, bool_equations)}")
# topo_ord = topological_sort(graph)
# draw_regular_graph(sub_g)
