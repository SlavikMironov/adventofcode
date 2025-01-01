from collections import Counter


def read_file_as_list(filename: str) -> tuple[list[int], list[int]]:
    with open(filename, "r") as file:
        arr1, arr2 = [], []
        for line in file:
            l1, l2 = line.split()
            arr1.append(int(l1))
            arr2.append(int(l2))
    return arr1, arr2


def difference_between_arrays(arr1: list[int], arr2: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(sorted(arr1), sorted(arr2)))


def similarity_score(arr1: list[int], arr2: list[int]) -> int:
    counters = Counter(arr2)
    return sum(num * counters[num] for num in arr1)


arr1, arr2 = read_file_as_list("input.txt")

# Part 1
print(f"Difference between arrays: {difference_between_arrays(arr1, arr2)}")

# Part 2
print(f"Similarity Score: {similarity_score(arr1, arr2)}")
