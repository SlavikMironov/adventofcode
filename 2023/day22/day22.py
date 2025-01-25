def get_puzzle(path):
    with open(path) as file:
        return list(
            list(
                list(map(int, coordinates.split(",")))
                for coordinates in line.split("~")
            )
            for line in file.read().splitlines()
        )


def part_one(puzzle):
    def overlap(p1, p2):
        # בדיקת חפיפה בין לבנה p1 ל-p2
        return (
            max(p1[0][0], p2[0][0]) <= min(p1[1][0], p2[1][0])
            and max(p1[0][1], p2[0][1]) <= min(p1[1][1], p2[1][1])
            and max(p1[0][2], p2[0][2]) <= min(p1[1][2], p2[1][2])
        )

    # מיון הלבנים לפי הגובה הנמוך ביותר (z)
    puzzle.sort(key=lambda t: min(t[0][-1], t[1][-1]))

    # יצירת מבנה נתונים למעקב אחרי המיקום הסופי של כל לבנה
    settled_positions = []
    max_z = 1  # הגובה המינימלי האפשרי

    for i in range(len(puzzle)):
        # נקודת התחלה
        current_z = min(puzzle[i][0][2], puzzle[i][1][2])
        is_overlap = False

        # בדיקה מול כל הלבנים שכבר התייצבו
        while current_z > max_z:
            is_overlap = False
            for j in range(len(settled_positions)):
                # אם יש חפיפה עם לבנה שכבר התייצבה, עצור
                if overlap(puzzle[i], settled_positions[j]):
                    is_overlap = True
                    break
            if not is_overlap:
                # אם אין חפיפה, המשך להוריד את הלבנה
                current_z -= 1
                puzzle[i][0][2] -= 1
                puzzle[i][1][2] -= 1
            else:
                break

        # שמירת המיקום הסופי של הלבנה
        settled_positions.append(puzzle[i])

    # חישוב ומחזיר את הגובה המקסימלי
    return max([p[2] for p in settled_positions])


# def part_one(puzzle):
#     def overlap(p1, p2):
#         return max(p1[0][0], p2[0][0]) <= min(p1[1][0], p2[1][0]) and max(
#             p1[0][1], p2[0][1]
#         ) <= min(p1[1][1], p2[1][1])

#     puzzle.sort(key=lambda t: min(t[0][-1], t[1][-1]))

#     max_z = 1

#     for i in range(len(puzzle)):
#         is_overlap = False
#         current_z = min(puzzle[i][0][2], puzzle[i][1][2])
#         for j in range(i):
#             if min(puzzle[j][0][2], puzzle[j][1][2]) == current_z:
#                 if overlap(puzzle[i], puzzle[j]):
#                     is_overlap = True
#                     break
#         if not is_overlap:
#             current_z -= 1


path = "input.txt"
puzzle = get_puzzle(path)
print(part_one(puzzle))
