with open('day_6.txt') as p:
    raw = p.read()
    passports: list[str] = raw.split("\n\n")

sum = 0
for i in passports:
    i = i.replace("\n", "")
    sum += len(set(i))

print("Part 1 solution", sum)

sum = 0
for i in passports:
    all_lines = i.split("\n")
    intersection = set(all_lines[0])
    for j in all_lines[1:]:
        intersection = intersection.intersection(j)
    sum += len(intersection)

print("Part 2 solution", sum)

