with open('day_7.txt') as p:
    raw = p.read()
    lines: list[str] = raw.split("\n")

# Part 1
from collections import defaultdict

contained_by = defaultdict(set)

for line in lines:
    line = line.replace('bags', 'bag')
    container, contents = line.split(' contain ')
    contents = [content.strip(" .").split(" ", 1)[1] for content in contents.split(',') if
                not content.startswith("no")]
    for content in contents:
        contained_by[content].add(container)

visited = set(contained_by['shiny gold bag'])
to_visit = list(contained_by['shiny gold bag'])

while to_visit:
    next = to_visit.pop()
    visited.add(next)
    to_visit.extend([bag for bag in contained_by[next] if bag not in visited])

print(len(visited))

contained_by = defaultdict(set)


# Part 2

def parse_contains_statement(contains_statement):
    count, bags = contains_statement.strip(" .").split(" ", 1)
    return int(count), bags


contains = defaultdict(list)

for line in lines:
    line = line.replace('bags', 'bag')
    container, contents = line.split(' contain ')
    contents = [
        parse_contains_statement(content)
        for content in contents.split(',')
        if not content.startswith("no")
    ]
    contains[container] = contents

start_key = 'shiny gold bag'


def total_bags(contains_relation, current_bag):
    sum = 0
    for rel_bag in contains_relation[current_bag]:
        num, bag = rel_bag
        sum += num + num * total_bags(contains_relation, bag)
    return sum


print(total_bags(contains, start_key))

