import math
import sys

sys.setrecursionlimit(10**7)  # Example: Set to 1,000,000


def get_input(path):
    with open(path) as file:
        game_machines = []
        machines = file.read().split("\n\n")
        for machine in machines:
            button_a, button_b, prize = machine.split("\n")
            ax, ay = button_a.lstrip("Button A: ").split(", ")
            bx, by = button_b.lstrip("Button B: ").split(", ")
            x, y = prize.lstrip("Prize: ").split(", ")
            ax = int(ax.split("+")[1])
            ay = int(ay.split("+")[1])
            bx = int(bx.split("+")[1])
            by = int(by.split("+")[1])
            x = int(x.split("=")[1])
            y = int(y.split("=")[1])
            game_machines.append(((ax, ay), (bx, by), (x, y)))
        return game_machines


def part_one_naive(machines):
    total_cost = 0

    def get_min_price(prize, a, b, A, B, memo=None):
        x, y = prize
        ax, ay = A
        bx, by = B
        if memo is None:
            memo = {}

        if prize in memo:
            return memo[prize]

        if prize == (0, 0):
            return 3 * a + b
        if x < 0 or y < 0:
            return float("inf")

        pa = get_min_price((x - ax, y - ay), a + 1, b, A, B, memo)
        pb = get_min_price((x - bx, y - by), a, b + 1, A, B, memo)

        memo[prize] = min(pa, pb)

        return memo[prize]

    for machine in machines:
        a_button, b_button, prize = machine
        price = get_min_price(prize, 0, 0, a_button, b_button)

        if not math.isinf(price):
            total_cost += price

    return total_cost


def part_two_naive(machines):
    total_cost = 0

    def get_min_price(prize, a, b, A, B, memo=None):
        x, y = prize
        ax, ay = A
        bx, by = B

        if prize in memo:
            return memo[prize]

        if prize == (0, 0):
            return 3 * a + b
        if x < 0 or y < 0:
            return float("inf")

        if memo is None:
            memo = {}

        pa = get_min_price((x - ax, y - ay), a + 1, b, A, B, memo)
        pb = get_min_price((x - bx, y - by), a, b + 1, A, B, memo)

        memo[prize] = min(pa, pb)

        return memo[prize]

    for machine in machines:
        a_button, b_button, prize = machine
        x, y = prize
        x += 10000000000000
        y += 10000000000000

        price = get_min_price((x, y), 0, 0, a_button, b_button)

        if not math.isinf(price):
            total_cost += price

    return total_cost


def part_one(machines):
    total_cost = 0

    for machine in machines:
        a_button, b_button, prize = machine
        ax, ay = a_button
        bx, by = b_button
        x, y = prize

        m = ax * by - ay * bx
        m1 = x * by - y * bx
        m2 = y * ax - x * ay

        a = m1 / m
        b = m2 / m
        if a // 1 == a and b // 1 == b:
            total_cost += 3 * a + b

    return total_cost


def part_two(machines):
    total_cost = 0

    for machine in machines:
        a_button, b_button, prize = machine
        ax, ay = a_button
        bx, by = b_button
        x, y = prize

        x += 10000000000000
        y += 10000000000000
        m = ax * by - ay * bx
        m1 = x * by - y * bx
        m2 = y * ax - x * ay

        a = m1 / m
        b = m2 / m
        if a // 1 == a and b // 1 == b:
            total_cost += 3 * a + b

    return total_cost


path = "input.txt"

machines = get_input(path)

print(f"Part one: {int(part_one_naive(machines))}")
print(f"Part two: {int(part_two(machines))}")
