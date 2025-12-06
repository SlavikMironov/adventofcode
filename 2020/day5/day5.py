seats = open("input.txt").read().splitlines()
max_id = float("-inf")
all_seats = []


def get_seat(seat):
    l1, r1 = 0, 127
    l2, r2 = 0, 7

    for i in range(7):
        m = (l1 + r1) // 2

        if seat[i] == "F":
            r1 = m
        else:
            l1 = m + 1

    for i in range(7, len(seat)):
        m = (l2 + r2) // 2

        if seat[i] == "L":
            r2 = m
        else:
            l2 = m + 1
    return l1, l2


for seat in seats:
    r, c = get_seat(seat)
    seat_id = r * 8 + c
    all_seats.append(seat_id)
    max_id = max(max_id, seat_id)

print(f"Part one: {max_id}")
all_seats.sort()

for i in range(1, len(all_seats)):
    if all_seats[i - 1] + 2 == all_seats[i]:
        print(f"Part two: {all_seats[i] - 1}")
        break
