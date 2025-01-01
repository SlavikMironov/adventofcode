from collections import defaultdict

Y = 16777216


def get_secret_numbers(path):
    with open(path) as file:
        return list(map(int, file.read().splitlines()))


def part_one(secret_numbers):
    s = 0
    for secret_number in secret_numbers:
        for _ in range(2000):
            secret_number = ((secret_number << 6) ^ secret_number) % Y
            secret_number = ((secret_number >> 5) ^ secret_number) % Y
            secret_number = ((secret_number << 11) ^ secret_number) % Y

        s += secret_number

    return s


def part_two(secret_numbers):
    max_bananas = 0
    all_changes_prices = defaultdict(int)

    for secret_number in secret_numbers:
        previous_price = secret_number % 10
        price_changes = []
        processed_sequences = set()

        for _ in range(2000):
            secret_number = ((secret_number << 6) ^ secret_number) % Y
            secret_number = ((secret_number >> 5) ^ secret_number) % Y
            secret_number = ((secret_number << 11) ^ secret_number) % Y

            last_digit = secret_number % 10
            change = last_digit - previous_price

            price_changes.append(change)

            if len(price_changes) > 4:
                price_changes = price_changes[1:]

            if len(price_changes) == 4:
                price_changes_key = tuple(price_changes)
                if price_changes_key not in processed_sequences:
                    all_changes_prices[price_changes_key] += last_digit
                    max_bananas = max(
                        max_bananas, all_changes_prices[price_changes_key]
                    )
                processed_sequences.add(price_changes_key)

            previous_price = last_digit

    return max_bananas


path = "input.txt"

secret_numbers = get_secret_numbers(path)
print(f"Part one: {part_one(secret_numbers)}")
print(f"Part two: {part_two(secret_numbers)}")
