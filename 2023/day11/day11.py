def get_maze(path):
    with open(path) as file:
        return file.read().splitlines()


def get_empty_cells(maze):
    empty_rows, empty_cols = [], []

    for row in range(len(maze)):
        row_galaxies = False
        col_galaxies = False
        for col in range(len(maze[0])):
            if maze[row][col] == "#":
                row_galaxies = True
            if maze[col][row] == "#":
                col_galaxies = True
        if not row_galaxies:
            empty_rows.append(row)
        if not col_galaxies:
            empty_cols.append(row)

    return empty_rows, empty_cols


def get_galaxies_coordinates(maze, empty_rows, empty_cols, expand=2):
    galaxies = []

    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "#":
                expand_rows, expand_cols, row_index, col_index = 0, 0, -1, -1

                for index, empty_row_index in enumerate(empty_rows):
                    if row > empty_row_index:
                        row_index = index
                for index, empty_col_index in enumerate(empty_cols):
                    if col > empty_col_index:
                        col_index = index

                expand_rows = (row_index + 1) * (expand - 1)
                expand_cols = (col_index + 1) * (expand - 1)

                galaxies.append((row + expand_rows, col + expand_cols))

    return galaxies


def part_one(maze):
    distances = 0
    empty_rows, empty_cols = get_empty_cells(maze)
    galaxies = get_galaxies_coordinates(maze, empty_rows, empty_cols)

    for i in range(len(galaxies)):
        for j in range(i + 1):
            g1r, g1c = galaxies[i]
            g2r, g2c = galaxies[j]

            distances += abs(g2r - g1r) + abs(g2c - g1c)

    return distances


def part_two(maze):
    distances = 0
    empty_rows, empty_cols = get_empty_cells(maze)
    galaxies = get_galaxies_coordinates(maze, empty_rows, empty_cols, 1000000)

    for i in range(len(galaxies)):
        for j in range(i + 1):
            g1r, g1c = galaxies[i]
            g2r, g2c = galaxies[j]

            distances += abs(g2r - g1r) + abs(g2c - g1c)

    return distances


path = "input.txt"

maze = get_maze(path)
print(f"Part one: {part_one(maze)}")
print(f"Part two: {part_two(maze)}")
