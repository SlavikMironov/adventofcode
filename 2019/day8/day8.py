pixels = open("input.txt").read()
w, t = 25, 6
n = w * t
digit1 = digit2 = zeros = count = 0
m = float("inf")
d1 = d2 = 0

for d in pixels:
    count += 1
    if d == "0":
        zeros += 1
    elif d == "1":
        digit1 += 1
    elif d == "2":
        digit2 += 1
    if count % n == 0:
        if zeros < m:
            m = zeros
            d1 = digit1
            d2 = digit2
        digit1 = digit2 = zeros = 0

print(f"Part one: {d1 * d2}\n")


image = [None] * n

for i in range(len(pixels)):
    if pixels[i] != "2" and image[i % n] == None:
        image[i % n] = "*" if pixels[i] == "1" else " "

print("Part two:")
for i in range(0, n, w):
    print("".join(image[i : i + w]))
