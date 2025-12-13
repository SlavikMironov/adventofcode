numbers = list(map(int, open("input.txt").read().splitlines()))
n = len(numbers)

preamble = set(numbers[:25])

for i in range(25, n):
    if all(numbers[i] - num not in preamble for num in preamble):
        target = numbers[i]
        print(f"Part one: {numbers[i]}")
        break
    preamble.remove(numbers[i - 25])
    preamble.add(numbers[i])

prefix = {0: -1}
s = 0

for i in range(n):
    s += numbers[i]
    t = s - target

    if t in prefix and i - prefix[t] > 1:
        j = prefix[t] + 1
        print(f"Part two: {min(numbers[j + 1:i + 1]) + max(numbers[j + 1:i + 1])}")
        break
    prefix[s] = i
