import copy

with open('day_11.txt') as p:
    seat_layout = [list(line.strip()) for line in p]


def print_layout(layout):
    for i in layout:
        print("".join(i))
    print()


def adjacent_seats(layout, position):
    for i in range(-1, 2):
        row = position[0] + i
        if row < 0 or row >= len(layout):
            continue
        for j in range(-1, 2):
            column = position[1] + j
            if column < 0 or column >= len(layout[i]) or (row, column) == position:
                continue
            yield layout[row][column]


def apply_rules(layout: list[list[str]]) -> (list[list[str]], bool):
    layout_changed = False
    new_layout = copy.deepcopy(layout)
    for row_id, row in enumerate(layout):
        for col_id, seat_status in enumerate(row):
            if seat_status == "L" and "#" not in adjacent_seats(layout, (row_id, col_id)):
                new_layout[row_id][col_id] = "#"
                layout_changed = True
            elif seat_status == "#":
                adjacent_occupied_count = 0
                for adj_seat in adjacent_seats(layout, (row_id, col_id)):
                    if adj_seat == "#":
                        adjacent_occupied_count += 1
                        if adjacent_occupied_count == 4:
                            new_layout[row_id][col_id] = "L"
                            layout_changed = True
                            break
    return new_layout, layout_changed




stable = False
print_layout(seat_layout)
layout = seat_layout

while not stable:
    layout, layout_changed = apply_rules(layout)
    stable = not layout_changed

print_layout(layout)

from collections import Counter

print("Part 1 solution", Counter(j for i in layout for j in i)["#"])


# Part 2
def visible_adjacent_seats(layout, position, debug=False):
    for i in range(-1, 2):
        row = position[0] + i
        if row < 0 or row >= len(layout):
            continue
        for j in range(-1, 2):
            column = position[1] + j
            if (row, column) == position:
                continue
            if row < 0 or row >= len(layout) or column < 0 or column >= len(layout[row]):
                continue
            visible_row, visible_col = row, column
            while layout[visible_row][visible_col] == ".":
                visible_row += i
                visible_col += j
                if visible_row < 0 or visible_row >= len(layout) or visible_col < 0 or visible_col >= len(layout[row]):
                    break
            else:
                yield layout[visible_row][visible_col]


def apply_rules_part_2(layout: list[list[str]]) -> (list[list[str]], bool):
    layout_changed = False
    new_layout = copy.deepcopy(layout)
    for row_id, row in enumerate(layout):
        for col_id, seat_status in enumerate(row):
            if seat_status == "L" and "#" not in visible_adjacent_seats(layout, (row_id, col_id)):
                new_layout[row_id][col_id] = "#"
                layout_changed = True
            elif seat_status == "#":
                adjacent_occupied_count = 0
                for adj_seat in visible_adjacent_seats(layout, (row_id, col_id)):
                    if adj_seat == "#":
                        adjacent_occupied_count += 1
                        if adjacent_occupied_count == 5:
                            new_layout[row_id][col_id] = "L"
                            layout_changed = True
                            break
    return new_layout, layout_changed

stable = False
print_layout(seat_layout)
layout = seat_layout

while not stable:
    layout, layout_changed = apply_rules_part_2(layout)
    stable = not layout_changed

print_layout(layout)

print(list(visible_adjacent_seats(layout, (1, 8), debug=True)))

print("Part 2 solution", Counter(j for i in layout for j in i)["#"])
