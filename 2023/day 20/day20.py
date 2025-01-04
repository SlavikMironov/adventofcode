from collections import defaultdict
from math import gcd
from functools import reduce


class flip_flop:
    def __init__(self, name):
        self.state = 0
        self.name = name

    def is_default(self):
        return self.state == 0

    def insert_pulse(self, pulse):
        if pulse == 0:
            self.state = 1 - self.state
            return self.state
        return None


class conjunction:
    def __init__(self, name):
        self.name = name
        self.connected = {}

    def is_default(self):
        return sum(self.connected.values()) == 0

    def add_connection(self, name):
        self.connected[name] = 0

    def get_state(self):
        return sum(self.connected.values()) == len(self.connected)

    def insert_pulse(self, name, pulse):
        self.connected[name] = pulse
        return 0 if self.get_state() else 1


def get_input(path):
    graph = {}
    inverse_graph = defaultdict(list)

    with open(path) as file:
        for line in file.read().splitlines():
            state, next_states = line.split(" -> ")
            if state[0] in "%&":
                if state[0] == "%":
                    graph[state[1:]] = {
                        "next_states": next_states.split(", "),
                        "module": flip_flop(state[1:]),
                    }
                else:
                    graph[state[1:]] = {
                        "next_states": next_states.split(", "),
                        "module": conjunction(state[1:]),
                    }
            else:
                graph[state] = {
                    "next_states": next_states.split(", "),
                    "module": "",
                }

        for state in graph:
            for next_state in graph[state]["next_states"]:
                if next_state in graph and isinstance(
                    graph[next_state]["module"], conjunction
                ):
                    graph[next_state]["module"].add_connection(state)
                inverse_graph[next_state].append(state)

    return graph, inverse_graph


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_multiple(numbers):
    return reduce(lcm, numbers)


def part_two(graph, inverse_graph):
    cycle_state = inverse_graph[inverse_graph["rx"][0]]
    times = {}
    lcm_states = []
    count = defaultdict(int)

    for i in range(10000000):
        current_states = [("broadcaster", 0)]

        while current_states:
            next_states = []
            for state, pulse in current_states:
                for next_state in graph[state]["next_states"]:
                    if pulse == 0:
                        if (
                            next_state in cycle_state
                            and next_state in times
                            and count[next_state] == 2
                        ):
                            lcm_states.append(i - times[next_state])
                        times[next_state] = i
                        count[next_state] += 1
                    if len(lcm_states) == len(cycle_state):
                        return lcm_multiple(lcm_states)
                    if next_state == "rx" and pulse == 0:
                        print(i + 1)
                        return i + 1
                    if next_state != "output" and next_state in graph:
                        module = graph[next_state]["module"]
                        if isinstance(module, conjunction):
                            next_pulse = module.insert_pulse(state, pulse)
                        else:
                            next_pulse = module.insert_pulse(pulse)
                        if next_pulse is not None:
                            next_states.append((next_state, next_pulse))

            current_states = next_states


def part_one(graph):

    high, low = 0, 0
    for i in range(1000):
        current_states = [("broadcaster", 0)]
        low += 1
        while current_states:
            next_states = []
            for state, pulse in current_states:
                for next_state in graph[state]["next_states"]:
                    if pulse == 0:
                        low += 1
                    else:
                        high += 1
                    if next_state == "rx" and pulse == 0:
                        print(i + 1)
                        return i + 1
                    if next_state != "output" and next_state in graph:
                        module = graph[next_state]["module"]
                        if isinstance(module, conjunction):
                            next_pulse = module.insert_pulse(state, pulse)
                        else:
                            next_pulse = module.insert_pulse(pulse)
                        if next_pulse is not None:
                            next_states.append((next_state, next_pulse))

            current_states = next_states

    return high * low


def get_graph(graph):
    gr = "strict digraph {\n"
    for state in graph:
        label = (
            "FF"
            if isinstance(graph[state]["module"], flip_flop)
            else ("CO" if isinstance(graph[state]["module"], conjunction) else "br")
        )
        for neighbor in graph[state]["next_states"]:
            gr += f"{state} -> {neighbor} [label={label}]\n"

    gr += "}"

    return gr


path = "input.txt"

graph, inverse_graph = get_input(path)
print(f"Part one: {part_one(graph)}")
print(f"Part two: {part_two(graph, inverse_graph)}")
