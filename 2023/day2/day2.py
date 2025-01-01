import re


def get_cubes_list(path):
    with open(path) as file:
        return file.read().split("\n")


def part_one(games):
    game_id_pattern = r"^Game\s*(\d+):\s*"
    red_pattern = r"(\d+)\s*red"
    green_pattern = r"(\d+)\s*green"
    blue_pattern = r"(\d+)\s*blue"
    s = 0

    for game in games:
        r = re.search(game_id_pattern, game)
        id = int(r.group(1))
        game = game[r.end() :]
        games_sets = game.split("; ")
        all_sets_are_valid = True

        for game_set in games_sets:
            reds = re.findall(red_pattern, game_set)
            greens = re.findall(green_pattern, game_set)
            blues = re.findall(blue_pattern, game_set)
            if not (
                sum(map(int, reds)) <= 12
                and sum(map(int, greens)) <= 13
                and sum(map(int, blues)) <= 14
            ):
                all_sets_are_valid = False
                break
        if all_sets_are_valid:
            s += id

    return s


def part_two(games):
    game_id_pattern = r"^Game\s*(\d+):\s*"
    red_pattern = r"(\d+)\s*red"
    green_pattern = r"(\d+)\s*green"
    blue_pattern = r"(\d+)\s*blue"
    s = 0

    for game in games:
        r = re.search(game_id_pattern, game)
        id = int(r.group(1))
        game = game[r.end() :]
        games_sets = game.split("; ")
        red_candidates = []
        green_candidates = []
        blue_candidates = []

        for game_set in games_sets:
            reds = re.findall(red_pattern, game_set)
            greens = re.findall(green_pattern, game_set)
            blues = re.findall(blue_pattern, game_set)
            red_candidates.append(sum(map(int, reds)))
            green_candidates.append(sum(map(int, greens)))
            blue_candidates.append(sum(map(int, blues)))

        s += max(red_candidates) * max(green_candidates) * max(blue_candidates)

    return s


path = "input.txt"

games = get_cubes_list(path)
print(f"Part one: {part_one(games)}")
print(f"Part two: {part_two(games)}")
