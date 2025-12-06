import sys


nums = list(map(int, open("input.txt").read().splitlines()))

target = 2020
seen = set()

for num in nums:
    if target - num in seen:
        print(f"Part one: {num * (target - num)}")
        break
    seen.add(num)

nums.sort()
seen = set(nums)
n = len(nums)
l, r = 0, len(nums) - 1

for i in range(n - 2):
    finish = False

    for r in range(i + 2, n):
        x = nums[i] + nums[r]
        if x >= target:
            break
        if target - x in seen:
            print(f"Part two: {nums[i] * nums[r] * (target - x)}")
            finish = True
            sys.exit()
