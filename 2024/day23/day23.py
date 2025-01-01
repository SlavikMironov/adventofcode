from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx


def get_input(path):
    with open(path) as file:
        graph = defaultdict(set)

        for set_computers in file.read().splitlines():
            first_computer, second_computer = set_computers.split("-")
            graph[first_computer].add(second_computer)
            graph[second_computer].add(first_computer)

        return graph


def draw_graph(graph_structure):
    graph = nx.Graph()

    for node, neighbors in graph_structure.items():
        for neighbor in neighbors:
            graph.add_edge(node, neighbor)

    plt.figure(figsize=(12, 10))
    nx.draw(
        graph,
        with_labels=True,
        node_color="skyblue",
        node_size=800,
        edge_color="gray",
        font_size=10,
        font_weight="bold",
    )
    plt.title("Undirected Graph Representation", fontsize=16)
    plt.show()


def subsets(nodes, index=None):
    if index is None:
        index = len(nodes) - 1
    if index < 0:
        return [[]]

    subsets_with_the_last = []
    subsets_without_the_last = subsets(nodes, index - 1)

    for subset in subsets_without_the_last:
        subsets_with_the_last.append(subset + [nodes[index]])

    return subsets_with_the_last + subsets_without_the_last


def get_sub_graph(nodes, graph):
    nodes_set = set(nodes)
    sub_graph = {}

    for node in nodes:
        sub_graph[node] = nodes_set & graph[node]

    return sub_graph


def is_clique(graph):
    n = len(graph)

    return sum(map(len, graph.values())) == n * (n - 1)


def part_one(graph):
    triangles = set()
    counters = {}
    condition = lambda node: node[0] == "t"
    nodes = set()

    for v in graph:
        for u in graph[v]:
            for w in graph[v]:
                if w != u and w in graph[u]:
                    # if condition(v) or condition(u) or condition(w):
                    triangles.add(tuple(sorted((v, u, w))))

                    nodes.add(v)
                    nodes.add(u)
                    nodes.add(w)

    for v, u, w in triangles:
        counters[v] = counters.get(v, 0) + 1
        counters[u] = counters.get(u, 0) + 1
        counters[w] = counters.get(w, 0) + 1

    return max(counters, key=lambda item: counters[item])


path = "input.txt"
graph = get_input(path)

node = part_one(graph)
nodes = [node] + list(graph[node])
sub_nodes = subsets(nodes)
sub_nodes.sort(key=len, reverse=True)

for sub_node in sub_nodes:
    sub_graph = get_sub_graph(sub_node, graph)
    if is_clique(sub_graph):
        print(",".join(sorted(sub_node)))
        draw_graph(get_sub_graph(sub_node, graph))
        break
