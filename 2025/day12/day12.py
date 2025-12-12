c = 0
for line in open("input.txt").read().splitlines():
    dimensions, indices = line.split(": ")
    w, h = dimensions.split("x")
    w = int(w)
    h = int(h)
    indices = list(map(int, indices.split(" ")))
    if w * h >= 9 * sum(indices):
        c += 1
    print(f"dimension: {w * h}, s: {9*sum(indices)}")
print(c)
