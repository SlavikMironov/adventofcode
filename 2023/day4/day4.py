from collections import Counter


def get_cards(path):
    with open(path) as file:
        games = []

        for row in file:
            row = row.strip()
            index = row.find(":")
            row = row[index + 1 :]
            numbers, winning_numbers = row.split("|")
            numbers = set(map(int, numbers.split()))
            winning_numbers = set(map(int, winning_numbers.split()))
            games.append((numbers, winning_numbers))

        return games


def part_two(cards):
    total_cards = 0
    cards_map = {}

    for i, game in enumerate(cards):
        numbers, winning_numbers = game
        winners = numbers & winning_numbers
        n = len(winners)
        cards_map[i + 1] = list(range(i + 2, min(i + 2 + n, len(cards) + 1)))

    stack = list(range(1, len(cards) + 1))
    total_cards = len(stack)

    while stack:
        winning_cards = cards_map[stack.pop()]
        total_cards += len(winning_cards)
        stack.extend(winning_cards)

    return total_cards


def part_one(cards):
    s = 0
    for game in cards:
        numbers, winning_numbers = game
        winners = numbers & winning_numbers
        n = len(winners)

        s += 1 << (n - 1) if n else 0

    return s


path = "input.txt"

cards = get_cards(path)
print(f"Part one: {part_one(cards)}")
print(f"Part two: {part_two(cards)}")
