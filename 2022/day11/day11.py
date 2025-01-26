import math


class Monkey:
    def __init__(self, items, operation, divisible, if_true, if_false):
        self.items = items
        self.operation = operation
        self.divisible = divisible
        self.if_true = if_true
        self.if_false = if_false
        self.inspects = 0


def get_puzzle(path):
    monkeys = []

    with open(path) as file:
        for monkey in file.read().split("\n\n"):
            lines = monkey.split("\n")
            items = list(map(int, lines[1].split(": ")[-1].split(", ")))
            operation = lines[2].split(" = ")[-1]
            divisible = int(lines[3].split()[-1])
            if_true = int(lines[4].split()[-1])
            if_false = int(lines[5].split()[-1])
            monkeys.append(Monkey(items, operation, divisible, if_true, if_false))

    return monkeys


def part_one(monkeys: list[Monkey]):
    for round in range(20):
        for monkey in monkeys:
            for old in monkey.items:
                monkey.inspects += 1
                new = eval(monkey.operation) // 3
                monkeys[
                    monkey.if_true if not new % monkey.divisible else monkey.if_false
                ].items.append(new)
            monkey.items = []
    monkeys.sort(key=lambda monkey: monkey.inspects, reverse=True)

    return monkeys[0].inspects * monkeys[1].inspects


def part_two(monkeys: list[Monkey]):
    lcm_value = 1
    for m in monkeys:
        lcm_value = math.lcm(lcm_value, m.divisible)

    for round in range(10000):
        for monkey in monkeys:
            for old in monkey.items:
                monkey.inspects += 1
                new = eval(monkey.operation)
                new = new % lcm_value
                monkeys[
                    monkey.if_true if not new % monkey.divisible else monkey.if_false
                ].items.append(new)
            monkey.items = []
    monkeys.sort(key=lambda monkey: monkey.inspects, reverse=True)

    return monkeys[0].inspects * monkeys[1].inspects


path = "input.txt"

monkeys = get_puzzle(path)
print(f"Part one: {part_one(monkeys)}")
monkeys = get_puzzle(path)
print(f"Part two: {part_two(monkeys)}")
