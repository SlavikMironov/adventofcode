res_part1 = res_part2 = 0

for line in open("input.txt").read().splitlines():
    password_range, letter, password = line.split()
    letter = letter[0]
    l, r = map(int, password_range.split("-"))

    if l <= password.count(letter) <= r:
        res_part1 += 1

    if (password[l - 1] == letter) ^ (password[r - 1] == letter):
        res_part2 += 1

print(f"Part one: {res_part1}")
print(f"Part two: {res_part2}")
