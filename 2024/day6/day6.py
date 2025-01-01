import sys

# Set a higher recursion limit if needed
sys.setrecursionlimit(10000)  # Adjust as needed


def get_map(path):
    with open(path, "r") as file:
        return [list(line.rstrip("\n")) for line in file]


def part_one_iterative(maze):
    count = 0
    position = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    rotate = {
        "^": (">", position[">"]),
        "v": ("<", position["<"]),
        "<": ("^", position["^"]),
        ">": ("v", position["v"]),
    }
    i, j = get_starting_position(maze)
    stack = [(i, j, maze[i][j])]
    while stack:
        row, col, current_position = stack.pop()
        if maze[row][col] != "X":
            count += 1
            maze[row][col] = "X"

        next_row, next_col = get_next_position(position[current_position], (row, col))
        if not (0 <= next_row < len(maze) and 0 <= next_col < len(maze[0])):
            return count
        if maze[next_row][next_col] == "#":
            next_direction, offset = rotate[current_position]
            next_row, next_col = get_next_position(offset, (row, col))
            stack.append((next_row, next_col, next_direction))
        else:
            stack.append((next_row, next_col, current_position))

    return count


def part_two(maze):
    count = 0
    row, col = get_starting_position(maze)

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == ".":
                maze[i][j] = "#"
                if check_if_cycle(maze, (row, col)):
                    count += 1
                maze[i][j] = "."

    return count


def check_if_cycle(maze, starting_position):
    position = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    rotate = {
        "^": (">", position[">"]),
        "v": ("<", position["<"]),
        "<": ("^", position["^"]),
        ">": ("v", position["v"]),
    }
    i, j = starting_position
    visited = set()
    stack = [(i, j, maze[i][j])]

    while stack:
        row, col, current_position = stack.pop()
        if (row, col, current_position) in visited:
            return True
        visited.add((row, col, current_position))

        next_row, next_col = get_next_position(position[current_position], (row, col))

        if not (0 <= next_row < len(maze) and 0 <= next_col < len(maze[0])):
            return False

        if maze[next_row][next_col] == "#":
            next_direction, offset = rotate[current_position]
            next_row, next_col = get_next_position(offset, (row, col))
            stack.append((next_row, next_col, next_direction))
        else:
            stack.append((next_row, next_col, current_position))

    return False


def part_one(maze):
    count = 0
    position = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    rotate = {
        "^": (">", position[">"]),
        "v": ("<", position["<"]),
        "<": ("^", position["^"]),
        ">": ("v", position["v"]),
    }
    i, j = get_starting_position(maze)

    def travels_maze(row, col, current_position):
        nonlocal count

        if maze[row][col] != "X":
            count += 1
            maze[row][col] = "X"
        next_row, next_col = get_next_position(position[current_position], (row, col))
        if (
            0 > next_row
            or next_row >= len(maze)
            or 0 > next_col
            or next_col >= len(maze[0])
        ):
            return
        if maze[next_row][next_col] != "#":
            travels_maze(next_row, next_col, current_position)
        else:
            next_rotate = rotate[current_position]
            next_row, next_col = get_next_position(next_rotate[1], (row, col))
            travels_maze(next_row, next_col, next_rotate[0])

    travels_maze(i, j, maze[i][j])

    return count


def get_next_position(dir, curr):
    return tuple(x + y for x, y in zip(dir, curr))


def get_starting_position(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] in ["^", ">", "<", "v"]:
                return row, col


# def part_two_not_good(maze, starting_position, s_position):
#     count = 0
#     position = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
#     rotate = {
#         "^": (">", position[">"]),
#         "v": ("<", position["<"]),
#         "<": ("^", position["^"]),
#         ">": ("v", position["v"]),
#     }
#     i, j = starting_position

#     def travels_maze(row, col, current_position):
#         nonlocal count, i, j
#         next_row, next_col = get_next_position(position[current_position], (row, col))
#         # if maze[row][col] not in ["O", "X"]:
#         #     maze[row][col] = "X"
#         next_rotate = rotate[current_position]
#         next_row_rotate, next_col_rotate = get_next_position(next_rotate[1], (row, col))
#         visited.add((row, col, current_position))
#         if row == 4 and col == 4:
#             print("test")
#         if maze[row][col] not in ["X", "O"]:
#             count += 1
#             maze[row][col] = "X"
#         if (
#             0 > next_row
#             or next_row >= len(maze)
#             or 0 > next_col
#             or next_col >= len(maze[0])
#         ):
#             return
#         if (
#             (next_row, next_col) != (i, j)
#             and (next_row_rotate, next_col_rotate, next_rotate[0]) in visited
#             and maze[next_row][next_col] != "O"
#         ):
#             count += 1
#             maze[next_row][next_col] = "O"

#         if maze[next_row][next_col] != "#":
#             travels_maze(next_row, next_col, current_position)
#         else:
#             next_rotate = rotate[current_position]
#             next_row, next_col = get_next_position(next_rotate[1], (row, col))
#             travels_maze(next_row, next_col, next_rotate[0])

#     travels_maze(i, j, s_position)

#     return count


path = "input.txt"
maze = get_map(path)
print(f"Part one: {part_one(maze)}")
maze = get_map(path)
print(f"Part two: {part_two(maze)}")
print("hi")
