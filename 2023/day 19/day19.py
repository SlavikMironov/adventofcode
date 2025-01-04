from collections import defaultdict
import math
import copy


class rule_range:
    def __init__(self, lower, upper, lower_inclusive=True, upper_inclusive=False):
        self.lower = lower
        self.upper = upper
        self.lower_inclusive = lower_inclusive
        self.upper_inclusive = upper_inclusive

    def contains(self, value):
        if self.lower_inclusive:
            lower_check = value >= self.lower
        else:
            lower_check = value > self.lower

        if self.upper_inclusive:
            upper_check = value <= self.upper
        else:
            upper_check = value < self.upper

        return lower_check and upper_check

    def inverse(self):
        return rule_range(
            -self.upper if math.isinf(self.upper) else self.upper,
            -self.lower if math.isinf(self.lower) else self.lower,
            (
                self.upper_inclusive
                if math.isinf(self.upper)
                else not self.upper_inclusive
            ),
            (
                self.lower_inclusive
                if math.isinf(self.lower)
                else not self.lower_inclusive
            ),
        )

    def intersection(self, other):
        if not other:
            return None
        if other.upper >= self.lower and other.lower <= self.upper:
            lower = max(self, other, key=lambda ins: ins.lower)
            upper = min(self, other, key=lambda ins: ins.upper)
            intr = rule_range(
                lower.lower, upper.upper, lower.lower_inclusive, upper.upper_inclusive
            )
            if intr.lower == intr.upper and (
                not intr.upper_inclusive or not intr.lower_inclusive
            ):
                return None
            return intr
        return None

    def interval_len(self):
        return (
            self.upper
            + (-1 if not self.upper_inclusive else 0)
            - (self.lower + (1 if not self.lower_inclusive else 0))
            + 1
        )

    def __repr__(self):
        lower_bound = "[" if self.lower_inclusive else "("
        upper_bound = "]" if self.upper_inclusive else ")"
        return f"{lower_bound}{self.lower}, {self.upper}{upper_bound}"


def get_input(path):
    with open(path) as file:
        states_dict = defaultdict(list)
        variables_list = []

        states, variables = file.read().split("\n\n")
        for state in states.splitlines():
            split_index = state.index("{")
            state_name = state[:split_index]
            states_conditions = state[split_index + 1 : -1].split(",")
            for condition in states_conditions[:-1]:
                if condition == "A":
                    states_dict[state_name].append(True)
                elif condition == "R":
                    states_dict[state_name].append(False)
                else:
                    range_condition, next_state = condition.split(":")
                    if range_condition[1] == ">":
                        states_dict[state_name].append(
                            (
                                range_condition[0],
                                rule_range(
                                    int(range_condition[2:]),
                                    float("inf"),
                                    False,
                                    False,
                                ),
                                next_state,
                            )
                        )
                    else:
                        states_dict[state_name].append(
                            (
                                range_condition[0],
                                rule_range(
                                    float("-inf"),
                                    int(range_condition[2:]),
                                    False,
                                    False,
                                ),
                                next_state,
                            )
                        )

                state[split_index + 1 :].split(":")

            states_dict[state_name].append(states_conditions[-1])

        for variables_set in variables.splitlines():
            variables_dict = {}
            for v in variables_set[1:-1].split(","):
                u, r = v.split("=")
                variables_dict[u] = int(r)
            variables_list.append(variables_dict)
        return variables_list, states_dict


def part_two(states):
    ranges_dict = {
        "x": rule_range(1, 4000, True, True),
        "m": rule_range(1, 4000, True, True),
        "a": rule_range(1, 4000, True, True),
        "s": rule_range(1, 4000, True, True),
    }
    accepted_ranges = []

    def dfs(ranges, state):
        if state == "A":
            accepted_ranges.append(copy.deepcopy(ranges))
            return
        if state == "R":
            return

        original_ranges = copy.deepcopy(ranges)
        conditions = states[state]

        for condition in conditions[:-1]:
            r_name, r_range, next_state = condition
            original_range = original_ranges[r_name]
            original_ranges[r_name] = original_range.intersection(r_range)

            dfs(original_ranges, next_state)

            original_ranges[r_name] = original_range.intersection(r_range.inverse())

        dfs(original_ranges, conditions[-1])

    dfs(ranges_dict, "in")

    return calculate_total_volume(accepted_ranges)


def calculate_total_volume(accepted_ranges):
    total_volume = 0

    for ranges in accepted_ranges:
        volume = 1

        for var_range in ranges.values():
            volume *= var_range.interval_len()
        total_volume += volume

    return total_volume


def part_one(variables_list, states):
    count = 0

    for variables in variables_list:
        current_state = "in"
        while True:
            conditions = states[current_state]
            if current_state in "AR":
                if current_state == "A":
                    count += sum(variables.values())
                break
            for condition in conditions[:-1]:
                if condition[1].contains(variables[condition[0]]):
                    current_state = condition[-1]
                    break
            else:
                current_state = conditions[-1]

    return count


path = "input.txt"
variables_list, states = get_input(path)


print(f"Part one: {part_one(variables_list, states)}")
print(f"Part two: {part_two(states)}")
