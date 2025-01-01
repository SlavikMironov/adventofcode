def get_input(path):
    with open(path) as file:
        return [list(map(int, line.split())) for line in file.read().splitlines()]


def part_two(sequences):
    firsts = 0

    for sequence in sequences:
        first_terms = []
        empty_sequence = False

        while not empty_sequence:
            empty_sequence = True
            differences_sequence = []
            first_terms.append(sequence[0])

            for i in range(1, len(sequence)):
                term = sequence[i] - sequence[i - 1]
                if term:
                    empty_sequence = False
                differences_sequence.append(term)
            sequence = differences_sequence
        x = 0
        for i in range(len(first_terms) - 1, -1, -1):
            x = first_terms[i] - x
        firsts += x

    return firsts


def part_one(sequences):
    last_terms = 0

    for sequence in sequences:
        final_terms = 0
        empty_sequence = False

        while not empty_sequence:
            empty_sequence = True
            differences_sequence = []
            final_terms += sequence[-1]

            for i in range(1, len(sequence)):
                term = sequence[i] - sequence[i - 1]
                if term:
                    empty_sequence = False
                differences_sequence.append(term)
            sequence = differences_sequence
        last_terms += final_terms

    return last_terms


path = "input.txt"
sequences = get_input(path)

print(f"Part one: {part_one(sequences)}")
print(f"Part two: {part_two(sequences)}")
