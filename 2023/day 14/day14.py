def get_input(path):
    with open(path) as file:
        return list(map(list, file.read().splitlines()))


def part_one(maze):
    count = 0

    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "O":
                row_index = row
                for k in range(row - 1, -1, -1):
                    if maze[k][col] == ".":
                        row_index = k
                    else:
                        break
                if row_index != row:
                    maze[row_index][col] = "O"
                    maze[row][col] = "."
                count += len(maze) - row_index

    return count


def part_two(maze):
    def move_rounded_rock(direction, position):
        i, j = position

        if direction == "up":
            row_index = i
            for k in range(i - 1, -1, -1):
                if maze[k][j] == ".":
                    row_index = k
                else:
                    break
            if row_index != i:
                maze[row_index][j] = "O"
                maze[i][j] = "."

        elif direction == "down":
            row_index = i
            for k in range(i + 1, len(maze)):
                if maze[k][j] == ".":
                    row_index = k
                else:
                    break
            if row_index != i:
                maze[row_index][j] = "O"
                maze[i][j] = "."

        elif direction == "right":
            col_index = j
            for k in range(j + 1, len(maze[0])):
                if maze[i][k] == ".":
                    col_index = k
                else:
                    break
            if col_index != j:
                maze[i][col_index] = "O"
                maze[i][j] = "."

        elif direction == "left":
            col_index = j
            for k in range(j - 1, -1, -1):
                if maze[i][k] == ".":
                    col_index = k
                else:
                    break
            if col_index != j:
                maze[i][col_index] = "O"
                maze[i][j] = "."

    # coordinates = {}
    # cycle_coordinates = {}
    # x = 0
    # for row in range(len(maze)):
    #     for col in range(len(maze[0])):
    #         if maze[row][col] == "O":
    #             maze[row][col] = str(x)
    #             coordinates[str(x)] = {"init": (row, col), "current": (row, col)}
    #             x += 1

    # org_maze = []
    # for row in maze:
    #     org_maze.append(row.copy())
    count = 0
    cycle = ["up", "left", "down", "right"]
    # for i in maze:
    #     print("".join(i))
    # print()
    for k in range(500):
        for index, c in enumerate(cycle):
            if c in ["up", "left"]:
                for row in range(len(maze)):
                    for col in range(len(maze[0])):
                        if maze[row][col] not in "#.":
                            move_rounded_rock(c, (row, col))
            else:
                for row in range(len(maze) - 1, -1, -1):
                    for col in range(len(maze[0]) - 1, -1, -1):
                        if maze[row][col] not in "#.":
                            move_rounded_rock(c, (row, col))

                # for rounded_rock in coordinates:
                #     if (
                #         coordinates[rounded_rock]["init"]
                #         == coordinates[rounded_rock]["current"]
                #     ):
            #     if rounded_rock not in cycle_coordinates:
            #         cycle_coordinates[rounded_rock] = (k, index)
            # if len(coordinates) == len(cycle_coordinates):
            #     print("found all cycles")
        print(f"Cycle: {k+1}\n")
        for i in maze:
            print("".join(i))
        print()

    return count


path = "input.txt"

ans = """..O#..............O#..##.....##..O#............OO#...................OOOOOOO##.#.....OO#.#.#...O#...
..................OOOOO#....#.#.#.#.#.#.....OOO#..#..OOO#.#.#....O#O#..........O#.#......OO#..O#..OO
....O#........OOO#.......OOO#....O#.#.....OOOOO#..#.....OOOO#.O#..O#.....#.#.#......OOOO#.....OO#.OO
.....OOOO##......###.O#..O#.#........OOOOO##......OOO#....#.....OOO#.......O###..O#.##.......OOOOOO#
#.....................OOOOOOOO#......O#.......OOOOO###.........OO#.#.........OOO#......OOO#.#..O##..
#..OO#...........OO#.........OOOOO#...O#...OOO#......#...OOOOO#..#....OO#.........#....#....O#.....O
#.OO#............OO#.OO#..........OOOO#.#...........OOOOOO##.OO#...OOO#......#......OOO#O#..#...##.O
.....OOO#......#....#.......OO#....OO#...#.OO#......OOOOOO##....OO#.......OOO##...............OOOOOO
.OO#............OOOO##.............OOOOOO#....OOOO##....OOOO#......O#.............OOOOOO#......#...O
..OO#.O#.......O#...#..O#...OO#.OO#O#....OOO#...OOO#..OOOO#...........OOOO#.......OOOO##.........#.O
##..#OO#.........O###.....OOOO##.O##....OOO#.O#.O#....OO#.......OOO#......OO#....OOO#...#......#..#.
............OOOO#....OO##.O#........OOO#..OOO#.......O#...OOOO#............OOOOOOOO#.........#......
.#..##O#...................OOOOOO#..O#..#........OOOOO#OO#..O##....O##..O#.....OO#O#...##..........O
..........OOOO#..#......OOO#.....OO#.OO###.....OOO#..O##...O##...O##.....O#....OOO#................O
........OOO#.......#....OOO#.O#....##...O#..O#.OO#....OO#.......OOO#.#..OO#..OOOO#.............##.#O
#...........OOOOO#...O#.##O#.............OOOOO##O#..O#....OO##.O#....OO#..O#.OO##..O##.#..........##
...OO##.....OO#.......OO#.O#.#.......O#...#....OO#......OOOOOO##..OO##..O#...#..O#............O#..#.
......OOOOO#.O#.........OO#...............OOOOO#O#O#....O##.........OOOO#.#......OOOOO#.#......##.#.
.###..O#..OOO#..#.........OOOOOOOO#.......##......OOOOOOO#....OOOO#.#...O#.#...OOO#..............OOO
.#.#.O#........OOOOO#..O#......OOOO#..#.#...O#.OO##.OOO#......OOO#...OOO#..##.#.#.#.O#.OO#..#...O#.O
.#..#................OOOOOOOOO#.......OO##......OOOOO##.OO##.#...O#.##.....O#......OOOO#O#.....OOOO#
...O#.O#..........OOOOOOOOOOO#..........OOO#......OOOOO#....O#...........OOO#.#.#..OO#.O#..O#...OOO#
.....OOOOO#..##.OOO#.....O#.OOO#......O#..................OOOOOOOO#............OOO#.O#...O#.O#....OO
.............OOOOOOOOOOOOOO###..........OOOOOOO#.OO#...O#....O#...OOO##......OOO#O#..O#......OO#...O
...OOOO##...OO#.O#.OO##..O#...#..OOO#....#....OOO#...............OOOOOOOOOO#.....#.........OOO#..#.O
OOO#.#.....OO#....OO#............OOOOOOOO#..OO#...OO#....OOOO##.O#....OOOO#.....#............OOOOOOO
.........OOOOOO#....OO#O#...OO#.OO#...##..OOO#......OOOOOOO#........OOOOO#......#.#...OOOOOOO#..OO#.
OO#.....O#....O#.#....OOO#O#...O#....O#.#....OOOOOO###...OOO#...OOO##....O#...#O#....OOOOO#..OOOOO#.
#.............OOOOOOOOO#......O#....OO#...OOO#..........OOOOOOOOOO##..O#....OO#O#.....OOOOOOOO#...OO
#OO#....OOOOO#...OOOO##...#.....O#...##..OO#O####..O#.##..#..O#O#..O#.......OOOO#..OOOOO#O#O###...OO
.O##O#...OO####.#.#....OOO#..O#.###...O#.##.O#.#.....O#..O#....OO#.O#....OO#.OOO#..OOOO#..O#...##...
.#.#....OO#.........#...###....O#..O##..#.#..O#........OOOO#...OO##..OO#.OO#..OOOOO#.OO#...........O
........OO#......#.O#......#.........OOOOOOOO#.OOOOO#.....OOOOOOO##.#OO#.OO#......OOOOOOO#........#.
.O#.......................OOOOOOO#..OO#.....OO#.O#.........OOOOOOOOOOOOOO#.##.O#.O##.O#...........#.
.#.OO##......O#....#........OO##..##..O#....O#..#....OOOOOOO#O##...#.OO##........OOO#.......OOO#....
...#.........OO#...#......O##..#............OOOOOOO#O#...........OOOO#..O#.OO#..O#.#.....#OO#.....OO
....#.#OO#....#.....#....#......OO###....O#.#....OOO#..O#...........OO#...O#.........OOOOO##......OO
................OO#............OO##........OOOOOO#...O#.#........OOOO#...#.O###.......OOOOO#.#.#...#
......#OO#........#..........O#.O#...............OOOOOOOO#..........OOOO#.##.#..O#O#....OOO#........
.......###.....................O#..O#.OO#..O#......................OOOOOOOOOOOOO#.##.O#...........OO
......#....................OO#..##..OO#......OOOOO#.O#.......OOOOOO#.O#.......O#......O#.....O##...O
.......................OOOOO#.....OO#.....OOO#O#..OOO##...OOO#O#.....................OOOO#.#..O#.#..
O#..................OO#....#...#.................OOOOOOOOOO##....OOO#.OOOO#........#....O##........O
..O#...O#...........#..O#.......OOO#..OOO#...##.O#.#.....OOOO#....OO##.OOOO#........O#.............O
#..#...##.................OOO###..#......OOOOO#.#...OO#.#......OOOOOO#O##O#...O#...........O#......O
...#..........OOO##.##..#...##.....#...........OOOOOOO#..OO#.O#.....OO#..#..O#...#..............OOOO
...OO#....O#...#..................O#..O##.....OO#.#.#....OO#.........OOOO#..#.....OOO##.......#.....
#...#.#..#.........OO#........O#..#..#.....OOO#......OOOO#..OO#..OOO#.#......#O#...#.....OOO#......O
.....#......O#......OOO##....#..........OOOO#...OO#.....OOO#.OO#............OO#............OOOOOOO#.
........#..O#.##..#..#..#.................OOOOO#.....OOO#....OOO#.O#.......OOO#..OOO#.##..O#......OO
........O#.............#...#..#.....OOO#..#....OO#.......OOO#.O#...OOO#........#.....OO#.........OOO
........O#...##.....O#..........O#....#.#............OOOOOOOO#.....O#....O#..............OOOOOOOO#..
#.............OOOO#.O#.........O#.......#O##.#......O#..........OO#.##.........OO#.......OO#..OO#.##
.#..........OOO#.#.#.O#..............#.........O#.................OOOOOOOO#........OOOO#......OOOO#.
...####...........#...OO#................##......#..O#.OOOO##..#..........O#.OOO##..O#.......OOOOO#.
.......OOOOO#.....O##......#...O#.#......#.......#..OOOOOO#...............OOOO#.........OOOOOOO#.#..
........OOOOOO#...#...........##................OOOOOOOOO#.....#.........OOO#..#.....OOOOO#........O
O#....OO#.O#...............OOO#.....OO##.............OOOOOOOOOO#.....OO#.......O#.#..#.#..OOO#..#...
#.....O#..#..........O#.#..#...O#..#..#..O#....OOO#O#.OO#......#..............OOOOOOO#.......OOOOOOO
......OO#....#....#.................OOOOOOOOOOO#...O#.............OOOOOOOOOOOOOO#...O#O#OO##O#.....O
#.#................OOO#.#..O#......#...#..O#O#.....OOO#..OOOO#..OOOO#.#.OO##...O#.OO#.###....OO#...O
...OOOO#............#O#.#..O#..........#...O#....OO##......OOOOO#..........OOOOOOOOO#....#.###.....O
##.###....#.........O####...........O#..#....##.#.....O#..##...OOO#O#...###.O#...OO#...#....#......O
.#.....O##.......OOOO###............O#.O#...O#.OO#.........O#.........OOOOOOO###..................OO
......#...#...O#.....OO#.#...........OOOOO#...##.....OOOOO#..OO#.O#......O#.#.#..#..#...#..#.#....O#
...........O#.........OOO#...OO#.#...O##.......OO#.#..#.#.O#.##..........OOOOOO#.....#....OO#....OO#
#............OOO#..#..#....#.#.....OOOO#OO#..............OOO#.O#.OO#....O#.###.......O#........OO##.
............O#..............OO#O#..................OOOOOO#.#...OOO#.#.........#......#O#.#...OO#.#..
.............O#....O#.....O#...#......OO#.............OOOOOOO#.OO#.........#.O#..#.#..##.........OOO
...#.#...#.#...#..............O#...........OOOOOO##...OO#...#...OO#........##....##...#...O#...OO#..
...#...........#................OO##...OOOO#.................OOOOOO#......................#..#O#...O
..O#.....O#.............OO##.#....OOO#.......OOOOOO#.........O#O#..................##.........#....O
#...O#........##.O#..#.OO#........OOOOO##.OO#.....O#.O#.......O#.......................#..........O#
...........O##.##.....##.....O#.OO#....OO#......OOO##....#..................OOO#......#...........OO
.........OOO#.....#....###.....O#..O#.#..O#.#.#....O#.#...#.........OOO#.#.#.#.....#......O#..#..OO#
.#....O###....#............#..........OO#.#.#...OOOO#.........O#.##....O#..........O#.#....OO#..#.#.
.O#....#........#.....#.#......OO#.......O#..O#.O##.......#...........OOOOO#......#...##.........OOO
..........OO#......O###.......OO#.......O#....O#....#...O#..O#.....O#....O#..#....#...#.....OOOOO#.#
........OOO##O#...#.#....#....O##..#....#..OOO#.O#..#.......OO#................OOOO#..OOOOO#.......O
.O#.....O#..##.............##...O#.......O#..........OOOOOO#...##...........OO#....###..O#.O#......#
.O#............................OO##.#...#.O##O#..O#....OO##.....#.......O#...#....#......O#......#O#
.....O#.....................OO#.##.........OO#.....OOO#..O#.....#....#.##.#..##...#..........OOOOO#.
..................OO#.........O##..#...O#.....OOOO#....O#.#.........................O#.##....#....OO
.....O#.#.#.#...........#...#.....O#...#.#.#...O#....#....#.......#........O#.......#.........O#..#.
..................O#....#..................OOOO##................#..##...O##.#.#..#....O##....#....O
.....OOO#...........#.....OO#....O#......O#....#..................OO#....#....#...........OOO#.#....
................OOOOOOO##..O#.....O#.................##........O#...................O##....#.......O
#....OO#.....##.OO#..#.....OO#..#.......OO#....................O#................O##...O#.....#.##..
..#.####...#...#O#....#..........O#.#..............OO#.#.......................#..#....O#.#.....#...
..#....O#O#.....#.......OO#...##.....#...............O#...............OO##.........O#.....#.........
....#..#.#...OO###...#.O#...................O#.....#.....#......O##.....O##..........O#.............
........OO#...O#.#....#.......OOOOO#.#.......#.......O#...#.#.....#...##......#.#.###............#..
#......O##.O#...#......#..OO#..#..O##...O#.......O#..O#.....#.............#......O#.#..#.......#...O
#....OO##..#.......#....##.#..#.#.O#.........O##...#...........#.........#....O##.#.......#.....#..O
......OOO#.....#.#.................OOO#............OOO#..#...O#...#O#......#..#...............O#...#
..#.OO#.O#.......#....#.#.......#..O#O#...OOO#..#......#.#..O#..............OOO#..##...#.##...#.....
.OO#.OO#...................#....O#..#####...#...#.......OO#....O##.O#..........###..#........#.....O
..OO##.#...........O#..#.#..#......#...#....O#....O#...........OOOO#.......#.......O#......OO#.##..#
OO#....#.#........................OOOO#.....OOO#.#...OOO#..##...........OOOOO#....#........##.....##
.OOO#.........OOOOOOO##........OOOOOOO#OOOO#.......O#O#.#......OOOO#O#...OOO#.........##..##...OO#.O"""
ans_maze = ans.splitlines()

count = 0

for row in range(len(ans_maze)):
    for col in range(len(ans_maze[0])):
        if ans_maze[row][col] == "O":
            count += len(ans_maze) - row
print(count)
maze = get_input(path)
# print(f"Part one: {part_one(maze)}")
# print(f"Part one: {part_two(maze)}")