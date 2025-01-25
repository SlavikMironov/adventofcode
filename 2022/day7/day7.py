from collections import defaultdict


class node:
    def __init__(self):
        self.neighbors = []
        self.file_sizes = 0
        self.directory_size = 0


def get_puzzle(path):
    with open(path) as file:
        return file.read().splitlines()


def solution(cmds):
    directories = defaultdict(node)
    current_dir = "/"
    i = 1

    while i < len(cmds):
        if cmds[i] == "$ ls":
            i += 1
            while i < len(cmds) and cmds[i][0] != "$":
                type, name = cmds[i].split()
                if type == "dir":
                    directories[current_dir].neighbors.append(
                        current_dir.rstrip("/") + "/" + name
                    )
                else:
                    directories[current_dir].file_sizes += int(type)
                i += 1
        if i < len(cmds) and cmds[i].startswith("$ cd"):
            name = cmds[i].split()[-1]
        if name == "..":
            current_dir = "/".join(current_dir.rstrip("/").split("/")[:-1]) or "/"
        else:
            current_dir = current_dir.rstrip("/") + "/" + name
        i += 1
    get_sizes_of_directories(directories)
    free_space = 70 * 10**6 - directories["/"].directory_size
    required_free_space = 30 * 10**6 - free_space

    dir_size = min(
        directory.directory_size
        for directory in directories.values()
        if directory.directory_size >= required_free_space
    )

    return (
        sum(
            directory.directory_size
            for directory in directories.values()
            if directory.directory_size <= 100000
        ),
        dir_size,
    )


def get_sizes_of_directories(directories, root="/"):
    def get_sizes(directory):
        for neighbor in directories[directory].neighbors:
            directories[directory].directory_size += get_sizes(neighbor)
        directories[directory].directory_size += directories[directory].file_sizes
        return directories[directory].directory_size

    get_sizes(root)


path = "input.txt"
cmds = get_puzzle(path)
print(f"Solution: {solution(cmds)}")
