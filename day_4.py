import re


def hgt_validator(x: str):
    num, unit = x[:-2], x[-2:]
    if unit == 'cm':
        return 150 <= int(num) <= 193
    elif unit == 'in':
        return 59 <= int(num) <= 76

    return False


REQ = {
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda x: x.isdigit() and len(x) == 9,
    'hcl': lambda x: bool(re.match("^#[0-9a-f]{6}$", x)),
    'hgt': hgt_validator
}

with open('day_4.txt') as p:
    raw = p.read()
    passports: list[str] = raw.split("\n\n")

# Part 1
valid = 0
for passport_str in passports:

    data = dict(
        field.split(":", 1) for field in passport_str.split()
    )

    if set(REQ).issubset(data):
        valid += 1

print("Part 1 solution", valid)

valid = 0

for passport_str in passports:

    data = dict(
        field.split(":", 1) for field in passport_str.split()
    )

    if not set(REQ).issubset(data):
        continue

    for i, validator in REQ.items():
        if not validator(data[i]):
            break
    else:
        valid += 1

print("Part 2 solution", valid)
