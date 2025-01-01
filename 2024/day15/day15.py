from queue import Queue


def get_input(path):
    with open(path) as file:
        grid, directions = file.read().split("\n\n")
        grid = [list(row) for row in grid.split("\n")]
        directions = list(directions.replace("\n", ""))

        return grid, directions


def part_one(grid, directions):
    s_r, s_c = get_starting_position(grid)
    directions_map = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    def move_blocks(row, col, direction):
        dr, dc = direction
        n_r, n_c = row + dr, col + dc

        while grid[n_r][n_c] == "O":
            n_r, n_c = n_r + dr, n_c + dc
        if grid[n_r][n_c] == "#":
            return False

        b_r, b_c = n_r - dr, n_c - dc
        while (n_r, n_c) != (row, col):
            grid[n_r][n_c], grid[b_r][b_c] = grid[b_r][b_c], grid[n_r][n_c]
            b_r, b_c = b_r - dr, b_c - dc
            n_r, n_c = n_r - dr, n_c - dc

        return True

    for direction in directions:
        dr, dc = directions_map[direction]
        nr, nc = s_r + dr, s_c + dc

        if grid[nr][nc] == ".":
            grid[nr][nc], grid[s_r][s_c] = grid[s_r][s_c], grid[nr][nc]
            s_r, s_c = nr, nc
        elif grid[nr][nc] == "O":
            if move_blocks(nr, nc, (dr, dc)):
                grid[nr][nc], grid[s_r][s_c] = grid[s_r][s_c], grid[nr][nc]
                s_r, s_c = nr, nc

    return sum(
        100 * i + j
        for i in range(len(grid))
        for j in range(len(grid[0]))
        if grid[i][j] == "O"
    )


def part_two(grid, directions):
    original_grid = []
    for row in range(len(grid)):
        original_row = []
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                original_row.append("#")
                original_row.append("#")
            if grid[row][col] == "O":
                original_row.append("[")
                original_row.append("]")
            if grid[row][col] == ".":
                original_row.append(".")
                original_row.append(".")
            if grid[row][col] == "@":
                original_row.append("@")
                original_row.append(".")
            # if grid[row][col] in "#.":
            #     original_row.extend([grid[row][col]] * 2)
            # elif grid[row][col] == "O":
            #     original_row.extend(["[", "]"])
            # elif grid[row][col] == "@":
            #     original_row.extend(["@", "."])
        original_grid.append(original_row)

    grid = original_grid
    s_r, s_c = get_starting_position(grid)
    directions_map = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
    s = 0

    def move_blocks(row, col, direction):
        dr, dc = direction
        n_r, n_c = row + dr, col + dc
        if direction in [(0, 1), (0, -1)]:
            while grid[n_r][n_c] in "[]":
                n_r, n_c = n_r + dr, n_c + dc
            if grid[n_r][n_c] == "#":
                return False

            b_r, b_c = n_r - dr, n_c - dc
            while (n_r, n_c) != (row, col):
                grid[n_r][n_c], grid[b_r][b_c] = grid[b_r][b_c], grid[n_r][n_c]
                b_r, b_c = b_r - dr, b_c - dc
                n_r, n_c = n_r - dr, n_c - dc

            return True
        else:
            blocks_to_move = get_shape(row, col, dr)
            if if_possible_to_move(blocks_to_move, dr):
                move(blocks_to_move, dr)
                return True
            else:
                return False

    def move(blocks_to_move, direction):
        for block in blocks_to_move[::-1]:
            row, col = block
            grid[row + direction][col] = grid[row][col]
            grid[row][col] = "."

    def get_shape(row, col, direction):
        blocks_to_move = []
        q = Queue()
        seen = set()

        if grid[row][col] == "[":
            q.put(((row, col), (row, col + 1)))
        else:
            q.put(((row, col - 1), (row, col)))

        while not q.empty():
            bl, br = q.get()
            blocks_to_move.extend([bl, br])

            if (
                grid[bl[0] + direction][bl[1]] == grid[bl[0]][bl[1]]
                and grid[br[0] + direction][br[1]] == grid[br[0]][br[1]]
            ):
                q.put((((bl[0] + direction, bl[1])), (br[0] + direction, br[1])))
            elif (
                grid[bl[0] + direction][bl[1]] == "]"
                and grid[br[0] + direction][br[1]] == "["
            ):
                q.put((((bl[0] + direction, bl[1] - 1)), (bl[0] + direction, bl[1])))
                q.put((((br[0] + direction, br[1])), (br[0] + direction, br[1] + 1)))
            elif grid[bl[0] + direction][bl[1]] == "]":
                q.put((((bl[0] + direction, bl[1] - 1)), (bl[0] + direction, bl[1])))
            elif grid[br[0] + direction][br[1]] == "[":
                q.put((((br[0] + direction, br[1])), (br[0] + direction, br[1] + 1)))

        return sorted(set(blocks_to_move), key=lambda t: direction * t[0])

    def if_possible_to_move(blocks_to_move, direction):
        set_of_blocks_to_move = set(blocks_to_move)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "#" and (i - direction, j) in set_of_blocks_to_move:
                    return False

        return True

    for direction in directions:
        dr, dc = directions_map[direction]
        nr, nc = s_r + dr, s_c + dc

        if grid[nr][nc] == ".":
            grid[nr][nc], grid[s_r][s_c] = grid[s_r][s_c], grid[nr][nc]
            s_r, s_c = nr, nc
        elif grid[nr][nc] in "[]":
            if move_blocks(nr, nc, (dr, dc)):
                grid[nr][nc], grid[s_r][s_c] = grid[s_r][s_c], grid[nr][nc]
                s_r, s_c = nr, nc

    return sum(
        100 * i + j
        for i in range(len(grid))
        for j in range(len(grid[0]))
        if j + 2 < len(grid[0]) and "".join(grid[i][j : j + 2]) == "[]"
    )


def get_starting_position(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@":
                return row, col


path = "input.txt"
grid, directions = get_input(path)

print(f"Part one: {part_one(grid, directions)}")
grid, directions = get_input(path)
print(f"Part two: {part_two(grid, directions)}")
