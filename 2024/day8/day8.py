from collections import defaultdict


def get_matrix(path: str) -> list[str]:
    with open(path, "r") as file:
        return [line.strip() for line in file]


def part_one(matrix: list[str]) -> int:
    antennas_coordinates = defaultdict(list)
    anti_nodes = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != ".":
                antennas_coordinates[matrix[row][col]].append(row + col * 1j)

    for coordinates in antennas_coordinates.values():
        calculate_anti_nodes(coordinates, matrix, anti_nodes)

    return len(anti_nodes)


def calculate_anti_nodes(
    coordinates: list[complex], matrix: list[str], anti_nodes_set: set[complex]
) -> None:
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            first_anti_node = 2 * coordinates[i] - coordinates[j]
            second_anti_node = 2 * coordinates[j] - coordinates[i]

            add_anti_node(anti_nodes_set, first_anti_node, len(matrix), len(matrix[0]))
            add_anti_node(anti_nodes_set, second_anti_node, len(matrix), len(matrix[0]))


def validate_coordinate(coordinate: complex, row_len: int, col_len: int) -> None:
    return 0 <= coordinate.real < row_len and 0 <= coordinate.imag < col_len


def add_anti_node(
    anti_nodes_set: set[complex], coordinate: complex, row_len: int, col_len: int
) -> None:
    if validate_coordinate(coordinate, row_len, col_len):
        anti_nodes_set.add(coordinate)


def part_two(matrix: list[str]) -> int:
    antennas_coordinates = {}
    anti_nodes = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != ".":
                antennas_coordinates.setdefault(matrix[row][col], [])
                antennas_coordinates[matrix[row][col]].append(row + col * 1j)

    for coordinates in antennas_coordinates.values():
        for i in range(len(coordinates) - 1):
            for j in range(i + 1, len(coordinates)):
                k = 1
                # First anti-node calculation
                first_anti_node = k * coordinates[i] - (k - 1) * coordinates[j]
                while validate_coordinate(first_anti_node, len(matrix), len(matrix[0])):
                    add_anti_node(
                        anti_nodes, first_anti_node, len(matrix), len(matrix[0])
                    )
                    k += 1
                    first_anti_node = k * coordinates[i] - (k - 1) * coordinates[j]

                k = 1
                # Second anti-node calculation
                second_anti_node = k * coordinates[j] - (k - 1) * coordinates[i]
                while validate_coordinate(
                    second_anti_node, len(matrix), len(matrix[0])
                ):
                    add_anti_node(
                        anti_nodes, second_anti_node, len(matrix), len(matrix[0])
                    )
                    k += 1
                    second_anti_node = k * coordinates[j] - (k - 1) * coordinates[i]

    return len(anti_nodes)


path = "input.txt"

matrix = get_matrix(path)

print(f"Part one: {part_one(matrix)}")
print(f"Part two: {part_two(matrix)}")
