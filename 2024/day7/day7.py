def get_input(path):
    with open(path, "r") as file:
        matrix = []
        for line in file:
            target, numbers = line.split(":")
            matrix.append((int(target), list(map(int, numbers.split()))))
        return matrix


def part_one(matrix):
    s = 0
    for row in matrix:
        target, nums = row
        if can_calibrate_v3(target, nums):
            s += target
    return s


def part_two(matrix):
    s = 0
    for row in matrix:
        target, nums = row
        if can_calibrate_v4(target, nums):
            s += target
    return s


def can_calibrate_dynamic(target, nums):
    table = [[False for _ in range(target + 1)] for _ in range(len(nums))]

    for t in range(len(table[0])):
        table[0][t] = nums[0] == t

    for t in range(target + 1):
        for i in range(1, len(table)):
            table[i][t] = table[i - 1][t - nums[i]] if t - nums[i] >= 0 else False
            table[i][t] |= table[i - 1][t // nums[i]] if t % nums[i] == 0 else False

    return table[len(nums) - 1][target]


def can_calibrate_recursive(target, nums):
    if not len(nums):
        return not target
    subtract = (
        can_calibrate_recursive(target - nums[-1], nums[:-1])
        if target >= nums[-1]
        else False
    )
    divide = (
        can_calibrate_recursive(target // nums[-1], nums[:-1])
        if target % nums[-1] == 0
        else False
    )

    return subtract or divide


def can_calibrate_recursive(target, nums):
    if not len(nums):
        return not target
    subtract = (
        can_calibrate_recursive(target - nums[-1], nums[:-1])
        if target >= nums[-1]
        else False
    )
    divide = (
        can_calibrate_recursive(target // nums[-1], nums[:-1])
        if target % nums[-1] == 0
        else False
    )

    return subtract or divide


def can_calibrate_v3(target, nums):
    if not nums:
        return False
    if len(nums) == 1:
        return target == nums[0]

    x = can_calibrate_v3(target, [nums[0] + nums[1]] + nums[2:])
    y = can_calibrate_v3(target, [nums[0] * nums[1]] + nums[2:])

    return x or y


def can_calibrate_v4(target, nums):
    if not nums:
        return False
    if len(nums) == 1:
        return target == nums[0]

    x = can_calibrate_v4(target, [nums[0] + nums[1]] + nums[2:])
    y = can_calibrate_v4(target, [nums[0] * nums[1]] + nums[2:])
    z = can_calibrate_v4(target, [int(str(nums[0]) + str(nums[1]))] + nums[2:])
    return x or y or z


def can_calibrate_v2(target, nums):
    memo = {}

    def helper(index, current_value):
        if index == len(nums):
            return current_value == target

        if (index, current_value) in memo:
            return memo[(index, current_value)]

        num = nums[index]
        add = helper(index + 1, current_value + num)
        multiply = helper(index + 1, current_value * num)
        concat = helper(index + 1, int(str(current_value) + str(num)))

        memo[(index, current_value)] = add or multiply or concat
        return memo[(index, current_value)]

    return helper(1, nums[0])


def can_calibrate_3_recursive(target, nums):
    if not len(nums):
        return not target
    if len(nums) == 1:
        return nums[0] == target
    subtract = (
        can_calibrate_3_recursive(target - nums[-1], nums[:-1])
        if target >= nums[-1]
        else False
    )
    divide = (
        can_calibrate_3_recursive(target // nums[-1], nums[:-1])
        if target % nums[-1] == 0
        else False
    )
    num_last = nums[-1]

    power = len(str(num_last))  # מספר הספרות של האיבר האחרון

    # עדכון המערך כך שכל איבר לפני האחרון מוכפל ב-10 בחזקת מספר הספרות של האיבר האחרון
    updated_nums = [(num * (10**power)) for num in nums[:-1]]

    # הוספת האיבר האחרון בחזרה למערך
    updated_nums.append(num_last)

    # מחסירים את האיבר האחרון מהמטרה ואז מבצעים קריאה חוזרת לרקורסיה
    concated = (
        can_calibrate_3_recursive(target - num_last, updated_nums[:-1])
        if target - num_last >= 0
        else False
    )

    return subtract or divide or concated


path = "input.txt"

matrix = get_input(path)
print(f"Part one: {part_one(matrix)}")
print(f"Part two: {part_two(matrix)}")
