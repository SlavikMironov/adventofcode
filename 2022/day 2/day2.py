GAME_SCORE = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
OPPONENT = {"A": "rock", "B": "paper", "C": "scissors"}
PLAYER = {"X": "rock", "Y": "paper", "Z": "scissors"}
SCORES = {"rock": 1, "paper": 2, "scissors": 3}


def get_puzzle(path):
    moves = []

    with open(path) as file:
        for g in file.read().splitlines():
            o, p = g.split()
            moves.append((OPPONENT[o], p))

    return moves


def part_one(puzzle):
    score = 0

    for o, p in puzzle:
        p = PLAYER[p]
        if p == o:
            score += 3
        elif GAME_SCORE[p] == o:
            score += 6
        score += SCORES[p]

    return score


def part_two(puzzle):
    score = 0

    for o, p in puzzle:
        if p == "X":
            p = GAME_SCORE[o]
        elif p == "Y":
            p = o
            score += 3
        else:
            p = GAME_SCORE[GAME_SCORE[o]]
            score += 6

        score += SCORES[p]

    return score


path = "input.txt"

puzzle = get_puzzle(path)
print(f"Part one: {part_one(puzzle)}")
print(f"Part two: {part_two(puzzle)}")
