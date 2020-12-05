with open('day_2.txt') as p:
    passwords: list[str] = list(p)

# Part 1
valid = 0

for password_and_policy in passwords:
    limits, char, password = password_and_policy.split()

    lower_limit, upper_limit = map(int, limits.split("-"))
    char = char[0]

    char_count = 0
    for c in password:
        if c == char:
            char_count += 1
            if char_count > upper_limit:
                break
    else:
        if char_count >= lower_limit:
            valid += 1


print("Valid passwords by rule 1", valid)

# Part 2
valid = 0

for password_and_policy in passwords:

    limits, char, password = password_and_policy.split()

    lower_limit, upper_limit = map(int, limits.split("-"))
    char = char[0]

    lower_condition = password[lower_limit - 1] == char
    upper_condition = password[upper_limit - 1] == char

    if (lower_condition or upper_condition) and not(lower_condition and upper_condition):
        valid += 1

print("Valid passwords by rule 2", valid)
