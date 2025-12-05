ranges, nums = open("input.txt").read().split("\n\n")
ranges = [list(map(int, range.split("-"))) for range in ranges.splitlines()]
nums = list(map(int, nums.splitlines()))
# Part 1
print(f"Part one: {sum(any(l <= num <= r for l, r in ranges) for num in nums)}")

# Part 2
ranges.sort()
curr_interval = ranges[0]
res = 0


for i in range(1, len(ranges)):
    if ranges[i][0] <= curr_interval[1]:
        r = max(curr_interval[1], ranges[i][1])
        curr_interval[1] = r
    else:
        res += curr_interval[1] - curr_interval[0] + 1
        curr_interval = ranges[i]
if curr_interval:
    res += curr_interval[1] - curr_interval[0] + 1

print(f"Part two: {res}")
