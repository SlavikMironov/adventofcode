from re import match, split

passports = open("input.txt").read().split("\n\n")
required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
res_part1 = res_part2 = 0
legal_passports = []
years_range = {"byr": (1920, 2002), "iyr": (2010, 2020), "eyr": (2020, 2030)}
color_eyes = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
m = {"cm": (150, 193), "in": (59, 76)}

for passport in passports:
    if all(key in passport for key in required_keys):
        legal_passports.append(passport)
        res_part1 += 1
print(f"Part one: {res_part1}")


def is_legal_year(val, l, r):
    return len(val) == 4 and val.isdecimal() and l <= int(val) <= r


def is_legal_height(val):
    height, unit = val[:-2], val[-2:]

    return unit in m and height.isdecimal() and m[unit][0] <= int(height) <= m[unit][-1]


def is_legal_hair_color(val):
    return match(r"^#[0-9a-f]{6}$", val) is not None


def is_legal_eyes_color(val):
    return val in color_eyes


def is_legal_passport_id(val):
    return match(r"^[0-9]{9}$", val) is not None


functions = {
    "hgt": is_legal_height,
    "hcl": is_legal_hair_color,
    "ecl": is_legal_eyes_color,
    "pid": is_legal_passport_id,
}


for passport in legal_passports:
    ok = True

    for key_val in split(r"\s", passport):
        key, val = key_val.split(":")

        if key in years_range:
            l, r = years_range[key]
            if not is_legal_year(val, l, r):
                ok = False
                break
        elif key == "cid":
            continue
        elif not functions[key](val):
            ok = False
            break

    res_part2 += ok


print(f"Part two: {res_part2}")
