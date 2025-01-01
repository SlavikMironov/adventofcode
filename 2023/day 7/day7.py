from collections import Counter

CARDS_MAP = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}


def get_cards(path):
    cards_list = []
    with open(path) as file:
        for cards_bid in file.read().splitlines():
            cards, bid = cards_bid.split()
            cards_list.append((cards, int(bid)))

        return cards_list


def part_two(cards_list: list[tuple[str, int]]):
    def sort_criteria(cards: tuple[str, int]):
        card_counters = Counter(cards[0])
        # most_card = card_counters.most_common(1)
        # cards = (cards[0].replace("J", most_card[0]), cards[1])
        # card_counters = Counter(cards[0])
        most_common_card = card_counters.most_common(1)[0][0]
        cards_order = tuple(count for _, count in card_counters.most_common(2))
        if len(cards_order) > 1:
            if most_common_card != "J":
                card_counters[most_common_card] += card_counters["J"]
                del card_counters["J"]
            elif most_common_card == "J":
                second_common_card = card_counters.most_common(2)[1][0]
                card_counters["J"] += card_counters[second_common_card]
                del card_counters[second_common_card]
        cards_order = tuple(count for _, count in card_counters.most_common(2))
        if len(cards_order) == 1:
            cards_order = (cards_order[0], 5)

        return cards_order + tuple(
            map(
                lambda card: (CARDS_MAP[card] if card in CARDS_MAP else int(card)),
                cards[0],
            )
        )

    cards_list.sort(key=sort_criteria)
    # print(cards_list)
    return sum((index + 1) * bid for index, (_, bid) in enumerate(cards_list))


def part_one(cards_list: list):
    def sort_criteria(cards):
        card_counters = Counter(cards[0])
        cards_order = tuple(count for _, count in card_counters.most_common(2))

        if len(cards_order) == 1:
            cards_order = (cards_order[0], 5)

        return cards_order + tuple(
            map(
                lambda card: (CARDS_MAP[card] if card in CARDS_MAP else int(card)),
                cards[0],
            )
        )

    cards_list.sort(key=sort_criteria)

    return sum((index + 1) * bid for index, (_, bid) in enumerate(cards_list))


path = "input.txt"

cards = get_cards(path)

print(f"Part one: {part_one(cards)}")
print(f"Part two: {part_two(cards)}")
