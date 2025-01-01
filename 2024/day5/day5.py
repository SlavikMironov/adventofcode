def get_input(path):
    with open(path, "r") as file:
        rules, pages = file.read().split("\n\n")
        return set(rules.split("\n")), list(
            map(lambda pages: pages.split(","), pages.split("\n"))
        )


def create_graph(rules):
    rules_graph = {}

    for rule in rules:
        x, y = rule.split("|")
        rules_graph.setdefault(x, [])
        rules_graph.setdefault(y, [])
        rules_graph[x].append(y)

    return rules_graph


def part_one(rules, pages):
    return sum(
        int(page[len(page) // 2]) for page in pages if validate_page(rules, page)
    )


def validate_page(rules, page):
    return all(
        f"{page[i]}|{page[j]}" in rules
        for i in range(len(page) - 1)
        for j in range(i + 1, len(page))
    )


def part_two(rules_graph, rules, pages):
    count = 0
    sub_rules_graph = {}

    for page in pages:
        if not validate_page(rules, page):
            all_p = set(page)
            for p in page:
                sub_rules_graph[p] = list(set(rules_graph[p]).intersection(all_p))
            t_order = topological_sort(sub_rules_graph)
            page.sort(key=lambda p: t_order[p])
            count += int(page[len(page) // 2])

    return count


def topological_sort(rules_graph):
    stack = []
    visited = set()

    def dfs(node):
        visited.add(node)

        for child in rules_graph[node]:
            if child not in visited:
                dfs(child)

        stack.append(node)

    for node in rules_graph:
        if node not in visited:
            dfs(node)

    return {node: index for index, node in enumerate(stack[::-1])}


path = "input.txt"
rules, pages = get_input(path)
rules_graph = create_graph(rules)

print(f"Part 1 :{part_one(rules, pages)}")
print(f"Part 2 :{part_two(rules_graph ,rules, pages)}")
