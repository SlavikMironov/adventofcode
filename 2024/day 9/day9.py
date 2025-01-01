def get_input(path):
    with open(path, "r") as file:
        return file.read().strip()


def part_one(puzzle):
    disk = []
    files_indices = []
    space_indices = []

    for i in range(0, len(puzzle), 2):
        file_block = int(puzzle[i])
        space_block = int(puzzle[i + 1]) if i < len(puzzle) - 1 else 0
        id = str(i // 2)
        for _ in range(file_block):
            disk.append(id)
            files_indices.append(len(disk) - 1)
        for _ in range(space_block):
            disk.append(".")
            space_indices.append(len(disk) - 1)

    k = 0
    for i in range(len(files_indices) - 1, -1, -1):
        file_index = files_indices[i]
        if k >= len(space_indices):
            break
        space_index = space_indices[k]
        if file_index < space_index:
            break
        disk[space_index], disk[file_index] = (
            disk[file_index],
            disk[space_index],
        )
        k += 1

    return sum(i * int(disk[i]) for i in range(len(disk)) if disk[i] != ".")


def part_two(puzzle):
    disk = []
    files_indices = []
    space_indices = []

    for i in range(0, len(puzzle), 2):
        file_block = int(puzzle[i])
        space_block = int(puzzle[i + 1]) if i < len(puzzle) - 1 else 0
        file_start_index = len(disk)
        disk.extend([str(i // 2)] * file_block)
        files_indices.append((file_start_index, file_start_index + file_block - 1))
        if space_block:
            space_start_index = len(disk)
            disk.extend(["."] * space_block)
            space_indices.append(
                (space_start_index, space_start_index + space_block - 1)
            )

    for i in range(len(files_indices) - 1, -1, -1):
        start_file, end_file = files_indices[i]
        file_length = end_file - start_file + 1

        for j in range(len(space_indices)):
            if not space_indices[j]:
                continue

            start_space, end_space = space_indices[j]
            space_length = end_space - start_space + 1

            if start_space > start_file:
                break

            if space_length >= file_length:
                # swap
                (
                    disk[start_space : start_space + file_length],
                    disk[start_file : end_file + 1],
                ) = (
                    disk[start_file : end_file + 1],
                    disk[start_space : start_space + file_length],
                )
                space_indices[j] = (
                    (start_space + file_length, end_space)
                    if space_length > file_length
                    else None
                )

                break

    return sum(i * int(disk[i]) for i in range(len(disk)) if disk[i] != ".")


path = "input.txt"

puzzle = get_input(path)

print(f"Part one: {part_one(puzzle)}")
print(f"Part two: {part_two(puzzle)}")
