puzzle = [int(line) for line in open("input.txt").read().splitlines()]

print(sum(fuel // 3 - 2 for fuel in puzzle))

total = 0

for fuel in puzzle:
    while fuel // 3 - 2 > 0:
        fuel = fuel // 3 - 2
        total += fuel

print(total)
