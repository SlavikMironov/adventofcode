problems = [line.split() for line in open("input.txt").read().splitlines()]
n, m = len(problems), len(problems[0])
res = 0

for j in range(m):
    operator = problems[-1][j]
    s, p = 0, 1
    for i in range(n - 1):
        num = int(problems[i][j])
        if operator == "+":
            s += num
        else:
            p *= num
    res += s if operator == "+" else p

print(f"Part one: {res}")

problems = open("input.txt").read().splitlines()
n, m = len(problems), len(problems[0])
res = 0
nums = []
num = []

for j in range(m - 1, -1, -1):
    for i in range(n - 1):
        if problems[i][j].isnumeric():
            num.append(problems[i][j])
    if num:
        nums.append(int("".join(num)))
        num = []
    if problems[-1][j] in "*+":
        if problems[-1][j] == "+":
            res += sum(nums)
        else:
            p = 1
            for num in nums:
                p *= num
            res += p
        num = []
        nums = []


print(f"Part two: {res}")
