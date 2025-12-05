ranges, nums = open("input.txt").read().split("\n\n")


ranges = [list(map(int, range.split("-"))) for range in ranges.splitlines()]
nums = list(map(int, nums.splitlines()))

res = 0

for num in nums:
    ok = False
    for l, r in ranges:
        if l <= num <= r:
            ok = True
            break

    if ok:
        res += 1
print(res)

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

print(res)
